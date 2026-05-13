import colorama
from colorama import Fore, Back, Style


colorama.init(autoreset=True)

ruyxat = {
    12 : {"ism": "Ali", "xona_turi": "Standart"}, 
    25 : {"ism": "Vali", "xona_turi": "Luxy"},
}

def mehmon_qoshish():
    print(f"\n{Fore.CYAN}{'='*30}")
    print(f"{Fore.CYAN}✨ YANGI MEHMON QO'SHISH ✨")
    print(f"{Fore.CYAN}{'='*30}\n")
    
    while True:
        ism = input(f"{Fore.YELLOW}👤 Ism: {Style.RESET_ALL}").title().strip()
        if ism == "":
            print(f"{Fore.RED}❌ Xato: Ism bo'sh bo'lishi mumkin emas!")
            continue
        
        try:
            xona_raqam = int(input(f"{Fore.YELLOW}🔑 Xona raqami: {Style.RESET_ALL}"))
        except ValueError:
            print(f"{Fore.RED}❌ Xato: Iltimos, faqat raqam kiriting!")
            continue

        if xona_raqam in ruyxat:
            print(f"{Fore.RED}⚠️ Bu joy band etilgan! Boshqa xona tanlang.")
            continue
            
        xona_turi_tanlov = input(f"""
{Fore.MAGENTA}🛋 Xona Turini tanlang:
1. Ekonom
2. Standart
3. Luxy
{Fore.YELLOW}Sevimli tanlovingiz: {Style.RESET_ALL}""")

        turlar = {"1": "Ekonom", "2": "Standart", "3": "Luxy"}
        
        
        tanlangan = turlar.get(xona_turi_tanlov) or (xona_turi_tanlov.capitalize() if xona_turi_tanlov.capitalize() in turlar.values() else None)

        if tanlangan:
            ruyxat[xona_raqam] = {"ism": ism, "xona_turi": tanlangan}
            print(f"\n{Fore.GREEN}✅ Muvaffaqiyatli: {ism} {xona_raqam}-xonaga joylashtirildi!")
            break
        else:
            print(f"{Fore.RED}❌ Xato: To'g'ri xona turini tanlang!")
            continue

def mehmon_uchirish():
    print(f"\n{Fore.RED}{'='*30}")
    print(f"{Fore.RED}🚪 MEHMONNI CHIQARISH 🚪")
    print(f"{Fore.RED}{'='*30}\n")
    
    delete_mehmon = input(f"{Fore.YELLOW}❓ Kim ketmoqchi: {Style.RESET_ALL}").title().strip()
    topilgan_xona = None
    
    for xona_raqam, malumot in ruyxat.items():
        if delete_mehmon == malumot['ism']:
            topilgan_xona = xona_raqam
            break
            
    if topilgan_xona:
        ruyxat.pop(topilgan_xona)
        print(f"{Fore.GREEN}✅ {delete_mehmon} ro'yxatdan o'chirildi. Xona {topilgan_xona} bo'shadi.")
    else:
        print(f"{Fore.RED}❌ Bunday mehmon topilmadi.")

def mehmon_ruyxat():
    print(f"\n{Fore.BLUE}{Style.BRIGHT}{'='*60}")
    print(f"{Fore.BLUE}{Style.BRIGHT}📋 MEHMONLAR RO'YXATI")
    print(f"{Fore.BLUE}{Style.BRIGHT}{'='*60}")
    
    # Jadval sarlavhasi
    header = f"{'Xona':<10} | {'Ism':<20} | {'Xona turi':<15}"
    print(f"{Fore.BLACK}{Back.WHITE}{header}")
    print("-" * 60)
    
    if not ruyxat:
        print(f"{Fore.YELLOW}📭 Mehmonxona hozircha bo'sh.")
    else:
        for xona, info in ruyxat.items():
            print(f"{Fore.CYAN}{xona:<10} {Fore.WHITE}| {info['ism']:<20} {Fore.WHITE}| {Fore.GREEN}{info['xona_turi']:<15}")
    
    print(f"{Fore.BLUE}{'='*60}\n")


while True:
    print(f"\n{Fore.YELLOW}🏨 {Style.BRIGHT}ASRTUM MEHMONXONASIGA XUSH KELIBSIZ!")
    choose_menyu = input(f"""
{Fore.CYAN}1 - ➕ Mehmon qo'shish
2 - ➖ Mehmonni chiqarish
3 - 📑 Mehmonlar ro'yxati
{Fore.RED}0 - 🛑 Chiqish

{Fore.YELLOW}➤ Buyruqni tanlang: {Style.RESET_ALL}""")

    if choose_menyu in ["1", "mehmon qo'shish"]:
        mehmon_qoshish()
    elif choose_menyu in ["2", "mehmoni ro'yxatdan chiqarish"]:
        mehmon_uchirish()
    elif choose_menyu in ["3", "mehmonlar ro'yxati"]:
        mehmon_ruyxat()
    elif choose_menyu in ["0", "dasturdan chiqish"]:
        print(f"\n{Fore.GREEN}✨ Vaqtingizni sarflaganingiz  uchun rahmat! Xayr! 👋")
        break
    else:
        print(f"{Fore.RED}❗ N oto'g'ri buyruq, qaytadan urinib ko'ring.")