#Imports
import time
import sys
from colorama import Fore, Back, Style, init
init(convert=True, autoreset=True)



# 1.*args va **kwargs

# def buyurtma_qabul_qilish(mijoz_ismi, *qoshimcha_ovqatlar, **manzil_malumotlari):
#     print(f"Mijoz: {mijoz_ismi}")
#     print(f"Qo'shimcha buyurtmalar: {qoshimcha_ovqatlar}")
#     print(f"Yetkazib berish manzili: {manzil_malumotlari}")

# buyurtma_qabul_qilish("Sardor", "Cola", "Frix", shahar="Samarqand", kocha="Amir Temur", uy=15)

2.

# def eng_kattasini_top(*args):
# 	max_son = max(args)
# 	return f" Eng katta son: {max_son}"

# print(eng_kattasini_top(1,42,5,20,5,88,8,8,9,20))

# # 2-Usul
# def eng_kattasini_top2(*args):
# 	max_son = args[0]
# 	for son in args:
# 		if son > max_son:
# 			max_son = son 

# 	return f"Eng katta son2: {max_son}"

# print(eng_kattasini_top2(1,42,-5,20,5,8,88,8,-99,20))


3.

# def avto_info(**kwargs):
# 	print(f"Kelgan ma'lumotlar: {kwargs}")
# 	for xususiyat,qiymat in kwargs.items():
# 		print(f"Xususisyat: {xususiyat}")
# 		print(f"Qiymat: {qiymat}")


		
# avto_info(rang="qora", yil=2023, narx=15000)


4.

def oquvchi_natijasi(ism, *baholar, **qoshimcha_malumotlar):
	umumiy_baho = sum(baholar)
	umumiy_baho = umumiy_baho / len(baholar)
	umumiy_malumot = f""" 
	=================================================
	                    Ism: {ism}
	=================================================
	                  Umumiy Baho: {umumiy_baho}
    -------------------------------------------------
	Qo'shimcha ma'lumotlar: {qoshimcha_malumotlar}
	--------------------------------------------------

	"""
	return umumiy_malumot

print(oquvchi_natijasi("ali", 4,4,3,5,4,3, sinfi=8, maktab=12))



# 5. ==============Decarators===============


# 1-Qadam: Dekoratorni (chexolni) yaratamiz



# def vaqt_olchovchi(asl_funksiya):
#     def wrapper(*args, **kwargs):
#         boshlanish_vaqti = time.time()
        
#         natija = asl_funksiya(*args, **kwargs) # Asl funksiyani ishga tushiramiz
        
#         tugash_vaqti = time.time()
#         print(f"⏱️ '{asl_funksiya.__name__}' funksiyasi {tugash_vaqti - boshlanish_vaqti} soniyada ishladi.")
        
#         return natija
#     return wrapper

# @vaqt_olchovchi
# def sonlarni_qoshish(a, b, c):
#     time.sleep(1) 
#     return a *b * c

# # Tekshiramiz
# print("Yig'indi:", sonlarni_qoshish(798645978645798645987654,9846597846598654,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))



6.  

# def chiroyli_salom(funksiya):
# 	def salom(*args, **kwargs):
# 		print("*"*20)
# 		print("Yangi xabar keldi!")
# 		funksiya(*args, **kwargs)
# 		print("Xabar muvaffaqiyatli yuborildi!")
# 		print("*"*20)
# 	return salom

# @chiroyli_salom
# def xabar_yoz(ism, xabar):
#     print(f"{ism}ga xabar: {xabar}")




# xabar_yoz("Qurbonali", "Salom")


7. 

# def faqat_adminlar_uchun(asl_func):
# 	def adminlar_tekshir(*args, **kwargs):
# 		lavozimm = kwargs.get("lavozim")
# 		if lavozimm == None and len(args) >= 2:
# 			lavozimm = args[1]
# 		if lavozimm.lower().strip() == "admin":
# 			asl_func(*args, **kwargs)
# 		else:
# 			print("Xatolik: Kechirasiz, sizda maxfiy bazaga kirish huquqi yo'q!")
# 	return adminlar_tekshir

# @faqat_adminlar_uchun
# def maxfiy_bazani_ochish(ism, lavozim):
#     print(f"Xush kelibsiz, {ism}! Mana siz so'ragan maxfiy ma'lumotlar...")

# user_name = input("Ismingiz: ")
# user_role = input("Lavozimingiz: ")
# maxfiy_bazani_ochish(user_name, user_role)


8. 

# def nolga_tekshiruvchi(func):
#     def wrapper(*args, **kwargs):
#         if 0 in args or 0 in kwargs.values():
#         	xato = "Nolga ko'paytirib bo'lmaydi!"
#         	return xato
#         else:
#         	result = func(*args,**kwargs)
#         	return result
#     return wrapper

# @nolga_tekshiruvchi
# def kopaytir(a, b):
#     return a * b


# a = int(input("Ko'paytirish uchun raqam kiriting: "))
# b = int(input("Qaysi raqamga ko'paytirmoqchisiz: "))
# print(kopaytir(a, b))  




# 9. Kosmik Stansiya Xavfsizlik Tizimi.


BANNER = Fore.CYAN + Style.BRIGHT
SUCCESS = Fore.GREEN + Style.BRIGHT
ERROR = Fore.RED + Style.BRIGHT
INFO = Fore.BLUE + Style.BRIGHT


def yuklanish_animatsiyasi(davomiyligi=30):  # Buni Ai orqali qildim faqat yuklanish animatsiyasini.Boshqasini emas.
    spinner = ['◜', '◠', '◝', '◞', '◡', '◟']
    print(f"{INFO}📡 Sun'iy yo'ldosh bilan aloqa o'rnatilmoqda...")
    
    for i in range(davomiyligi + 1):
        belgi = spinner[i % len(spinner)]
        foiz = int((i / davomiyligi) * 100)
        
        sys.stdout.write(f"\r{INFO}{belgi} Yuklanmoqda: {foiz}%")
        sys.stdout.flush() 
        
        time.sleep(0.1)
    
    sys.stdout.write(f"\r{' ' * 50}\r") 
    sys.stdout.flush()
    print(f"{SUCCESS}✅ Aloqa muvaffaqiyatli o'rnatildi!")

def xavfsizlik_filtri(funk):
    def parol_tekshirish(*args, **kwargs):
        kod = kwargs.get("kod")
        log = kwargs.get("ism")
        
        if kod == None or len(args) >= 2:
            log = args[0]
            kod = args[1]
            
        
        yuklanish_animatsiyasi()

        if log == None or log == "":
            return f"\n{ERROR}┌──────────────────────────────────────────┐\n" \
                   f"{ERROR}│ [!] XATO: Shaxsingizni tasdiqlang!       │\n" \
                   f"{ERROR}└──────────────────────────────────────────┘"
        
        elif log.title() == "Ilon Mask":
            return f"\n{Fore.YELLOW}⚠️  DIQQAT! XAVFSIZLIK TIZIMI REAKSIYASI:\n" \
                   f"{ERROR}────────────────────────────────────────────\n" \
                   f"{ERROR}Kechirasiz janob Mask, kirish taqiqlangan! \n" \
                   f"{ERROR}────────────────────────────────────────────"
        
        elif kod.strip() == "Mars-2026":
            natija = funk(*args, **kwargs)
            return f"\n{SUCCESS}🚀 [ TIZIMGA KIRILDI ]\n" \
                   f"{SUCCESS}╚══▶ {natija}"
        
        else:
            return f"\n{ERROR}❌ [ XATO ] PAROL NOTO'G'RI!\n" \
                   f"{ERROR}🚨 Xavfsizlik xizmati yo'lda..."
            
    return parol_tekshirish

@xavfsizlik_filtri
def shlyuzni_ochish(ism, kod):
    return f"Eshik ochildi. Xush kelibsiz, {ism}!"


print(f"{BANNER}==========================================")
print(f"{BANNER}🚀 MARS-1: KOSMIK TERMINAL ")
print(f"{BANNER}==========================================")

name = input(f"{INFO}👤 Ismingizni kiriting: {Style.RESET_ALL}")
password = input(f"{INFO}🔑 Kodingizni kiriting: {Style.RESET_ALL}")


print(shlyuzni_ochish(name, password))