from colorama import Fore, Back, Style, init
init(convert=True, autoreset=True)
import random

# 1.Global chaqirish

# a = 4  #global

# def f1():
# 	print(a)

# def f2():
# 	global a 
# 	a+=1
# 	print(a)

# f1()
# f2()

# 2.Local Scope
# l = [1,2,3,4,5] ->  #Global  

# def f1():
# 	l = [1,2,3,4,5]  #local -> funksiya ichida yaratiladi. 
# 	print(l)

# f1()

# 3.Nonlocal Scope

# def f1():
# 	a = 4  
# 	def f2(): #inner function -> ichma ich funksiya
# 		return a  #nonlocal


# 4. Global vs Local

# a = 4 # -> Global
# def f1():
# 	global a
# 	a = 5 
# 	return a# local -> 5

# print(a, "-> Global ") #global -> 4
# print(f1(), "-> Local") 


# 5.Ichma ich funksiyada Localni uzgartirish.

# def f1():
# 	a = 4  
# 	def f2(): #inner function 
# 		nonlocal a
# 		a += 2
# 	print(a)  # -> 6

# f1() 
# f2() # -> ishlamaydi!

# 6.Funksiyani Uzgaruvchiga tenglash.

# def s():
# 	a = 5
# 	return a

# x = s()
# print(x)


# def k(a):
# 	def q(b):
# 		return b
# 	return q

# a = 10
# b = 5

# Q = k(b)
# result = Q(a)
# print(result)
# # 2 - usul
# d = k(a)(b)
# print(d)



# def f(x):
#     def g(y):
#         def h(z):
#             return z
#         return h
#     return g
# a = 5
# b = 2
# c = 1
# print(f(a)(b)(c))


# def Q(a):
# 	b = 10
# 	def K(c):
# 		return a*b*c
# 	return K
# s = 10
# d = 2
# n = Q(s)
# natija = n(d)
# print(natija)


# def ok(a):
# 	x = 10
# 	return lambda y: x*y//a 
	
# a = 5
# y = 3
# h = ok(a)
# print(h(3))



# def compose(g, f):
#     def h(*args, **kwargs): #closure funksiya
#         return g(f(*args, **kwargs))
#     return h


# km_to_m= lambda x: x*1000
# m_to_sm= lambda x: x * 100

# km_to_sm = compose(m_to_sm, km_to_m)
# print(km_to_sm(13))   # Output 1 200 000


# 7. Counter Closure

# def sanoqchisni_yarat():
# 	sanoq = 0
# 	def ikkinchi_func():
# 		nonlocal sanoq
# 		sanoq += 1
# 		return sanoq
# 	return ikkinchi_func

# sanoqchi_1 = sanoqchisni_yarat()
# sanoqchi_2 = sanoqchisni_yarat()
# print(sanoqchi_1())
# print(sanoqchi_1())
# print(sanoqchi_1())
# print(sanoqchi_1())
# print("-"*20)
# print(sanoqchi_2())
# print(sanoqchi_2())
# print(sanoqchi_2())




# 8.🏰 "Zulmat Qasri" o‘yini loyihasi

TOP = Fore.CYAN + Style.BRIGHT
BANNER = Fore.RED + Style.BRIGHT
PROMPT = Fore.YELLOW + Style.BRIGHT
MENU = Fore.MAGENTA + Style.BRIGHT
INFO = Fore.BLUE + Style.NORMAL
ERROR = Fore.RED + Style.BRIGHT
OQ = Fore.WHITE + Style.BRIGHT
YASHIL = Fore.GREEN + Style.BRIGHT
RESET = Style.RESET_ALL

def qahramon_yarat(ism, quvvat):
    oltin = 0
    tajriba = 0
    daraja = 1
    def harakat_qil(buyruq):
        nonlocal quvvat,oltin,tajriba,daraja
        if buyruq.lower() in ["jang","1"]:
            quvvat -= random.randint(5, 40)
            oltin += random.randint(5, 30)
            tajriba += random.randint(5, 25) 
            if tajriba > 25:
            	daraja += 1
            print(Fore.WHITE + Style.BRIGHT + f"Jang natijasi — Quvvat: {quvvat}, Oltin: {oltin},Tajriba: {tajriba}, Daraja: {daraja}" + RESET)
            return quvvat
        elif buyruq.lower() in ["dam", "2"]:
            quvvat += 15
            if quvvat > 100: 
            	quvvat = 100
            	print(ERROR + "Maximum Quvvat" + RESET)
            print(INFO + f"Dam oldingiz. Yangi quvvat: {quvvat}" + RESET)
            return quvvat
        elif buyruq.lower() in ["holat", "3"]:
            print(MENU + f"Holat — Ism: {ism}; Quvvat: {quvvat}; Oltin: {oltin}, Tajriba: {tajriba}, Daraja: {daraja}" + RESET)
            return quvvat
        elif buyruq.lower() in ["do'kon", "4"]:
        	print(TOP + "\n╔" + "═"*45 + "╗")
        	print(TOP + "║" + PROMPT + "      🛒 ZULMAT BOZORI — SAVDO RASTASI 🛒    " + TOP + "║")
        	print(TOP + "╠" + "═"*45 + "╣")
        	print(TOP + "║ " + YASHIL + " 1. 🧪 Sehrli Damlama (+25 HP) " + PROMPT +  " 💰 30 Oltin " + TOP + "║")
        	print(TOP + "║ " + YASHIL + " 2. ⚔️ O‘tkir Qilich (+15 ATK)  " + PROMPT +  "💰 50 Oltin " + TOP + "║")
        	print(TOP + "║ " + YASHIL + " 3. 🍗 Qirol Kabobi (+60 HP)   " + PROMPT +  " 💰 70 Oltin " + TOP + "║")
        	print(TOP + "║ " + YASHIL + " 4. 🛡️ Temir Qalqon (+20 DEF) " + PROMPT +  " 💰 80 Oltin " + TOP + "║")
        	print(TOP + "╠" + "═"*45 + "╣")
        	print(TOP + "║ " + BANNER + " 0. 🚪 Bozordan chiqish                     " + TOP + "║")
        	print(TOP + "╚" + "═"*45 + "╝")
        	print(OQ + f"   💰 Sizning hamyoningizda: " + PROMPT + f"{oltin}" + OQ + " oltin bor." + RESET)
        	while True:
	        	xarid = input(INFO + "Nima Xarid qilmoqchisiz? " + RESET)
	        	if xarid.lower() in [ "sehrli damlama", "1"]:
	        		if oltin >= 30:
	        			oltin -= 30
	        			quvvat += 25
	        			print(YASHIL + f"Tabriklaymiz, Siz Sehrli Damlamani sotib oldingiz,\n Sizga 30 oltin evaziga 25 HP qo'shib berildi. Sizning Quvvatingiz: {quvvat}" + RESET)
	        			return quvvat
	        		else:
	        			print(BANNER + "Sizning Hisobingizda yetarli oltin yo'q!" + RESET)
	        			return quvvat
	        	elif xarid.lower() in ["o‘tkir qilich", "2"]:
	        		if oltin >= 50:
	        			oltin -= 50
	        			print(INFO + "Tabriklaymiz, Siz O'tkir Qilichni sotib oldingiz,\n Sizga 50 oltin evaziga 15 ATK qo'shib berildi." + RESET)
	        			return quvvat
	        		else:
	        			print(BANNER + "Sizning Hisobingizda yetarli oltin yo'q!" + RESET)
	        			return quvvat
	        	elif xarid.lower() in ["qirol kabobi", "3"]:
	        		if oltin >= 70:
	        			oltin -= 70
	        			quvvat += 60
	        			print(YASHIL + f"Tabriklaymiz, Siz Qirol Kabobini sotib oldingiz,\n Sizga 70 oltin evaziga 60 HP qo'shib berildi. Sizning Quvvatingiz: {quvvat}" + RESET)
	        			return quvvat
	        		else:
	        			print(BANNER + "Sizning Hisobingizda yetarli oltin yo'q!" + RESET)
	        			return quvvat
	        	elif xarid.lower() in ["temir qalqon", "4"]:
	        		if oltin >= 80:
	        			oltin -= 80
	        			print(INFO + "Tabriklaymiz, Siz Temir Qalqonni sotib oldingiz,\n Sizga 80 oltin evaziga 20 DEF qo'shib berildi." + RESET)
	        			return quvvat
	        		else:
	        			print(BANNER + "Sizning Hisobingizda yetarli oltin yo'q!" + RESET)
	        			return quvvat
	        	elif xarid.lower() in ["bozordan chiqish", "0"]:
	        		return quvvat 
	        		
	        	else:
	        		print(ERROR + "Noto‘g‘ri buyruq!" + RESET)
	        		return quvvat
        else:
            print(ERROR + "Noto‘g‘ri buyruq. Iltimos, 1, 2, 3 yoki jang/dam/holat yozing." + RESET)
            return quvvat
    return harakat_qil


print(
    BANNER + """
     ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓
    ▓  🏰Zulmat Qasri  — O'yinga xush kelibsiz  ▓ 
     ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ 
    """ + RESET
)

ism = input(
    TOP + """
    ║ ═══════════════════════════════════════ ║
   ║    Ismingizni kiriting (masalan: Ali): _  ║
    ║ ═══════════════════════════════════════ ║
    """ + RESET
)
quvvat = 100
result = qahramon_yarat(ism, quvvat)

while True:
    kerakli_menyu = input(
        PROMPT + """
       ┌──────────────────────────────┐
       │    Kerakli menyuni tanlang   │
       └──────────────────────────────┘
         ✦ 1. Jang
         ✦ 2. Dam
         ✦ 3. Holat
         ✦ 4. Do'kon
         

    Tanlovingiz: """ + RESET
    )
    hozirgi_quvvat = result(kerakli_menyu)
    if hozirgi_quvvat <= 0:
        print(ERROR + "O'yin tugadi! Sizning qahramoningiz quvvatsiz qoldi." + RESET)
        break
   

