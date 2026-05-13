# =====================IF | ELSE operatorlari====================


# Ob-Havo malumotlari:

print("Assalomu aleykum🤗. Ob-Havo haqida ma'lumot beradigan dasturimizga xush kelibsiz🌦")
ism = input("Ismingiz: ")
manzil = input("Qayerda yashaysiz: ")
soat = input("Soat nechi? ")
if soat == str:
	print("Xato⚠")
	soat = int(input("Soat nechi? "))

degree = int(input("Bugun Ob-Havo nechi gradus (℃): "))
while degree == int:
	print("Faqat raqam ko'rinishida kiriting⚠")
	degree = int(input("Bugun Ob-Havo nechi gradus (℃): "))
if degree < 0:
	print(f"Ob-Havo bugun {manzil}-da  sovuq ekan🥶")
elif degree > 0 and degree < 20:
	print(f"{ism} bugun {manzil} - da havo salqin ekan🙂")
elif degree > 21 and degree < 30:
	print(f"Bugun {manzil} da havo {soat} - da {degree} ℃ tashkil qiliadi. bu yer salqin degan statistikaga mos keladi.") 
elif degree > 31 and degree < 55 :
	print(f"Sizga bugun sabr tilayman chunki bugun {manzil}-da soat: {soat} da havo juda issiq🥵")
elif degree > 55 :
	print("Siz mabodo Venerada yashamaysizku😅")
else:
	print("To'g'ri formatda yozing!")

keying = """

       Keyingisi →

"""
print(keying)

# 2. Internet-do'kon Chegirmasi

paket_50 = """

50.000 - 100.000 gacha narxdagi paketlar:

📍Agar siz shu narxdagi paketlarni xarid qilsangiz 
kompaniyamiz sizga 5% chegirma qilib beradi💸. 

"""
paket_100 = """

100.000 - 150.000 gacha narxdagi paketlar:

📍Agar siz shu narxdagi paketlarni xarid qilsangiz 
kompaniyamiz sizga 10% chegirma qilib beradi💸.

"""
chegirma_50 = 50000
chegirma_60 = 60000
print("Assalomu aleykum🤗")
print("Bizning  Internet-do'konga xush kelibsiz 🤗")
xarid_summasi = int(input("Siz qanchaga paket xarid qilmoqchisiz? "))
if xarid_summasi <= 30000:
	print("Bunday miqdorda paket ham chegirma ham yo'q! ❌")
elif xarid_summasi > 30000 and xarid_summasi <50000:
	print("Bunday miqdorda paket ham chegirma ham yo'q! ❌")
elif xarid_summasi >= 50000 and xarid_summasi <= 100000:
	print("Ajoyib🥳. Bu so'mada bizda paket ham chegirmaham bor: ")
	print(paket_50)
	chegirma = int(input("Aynan qanchaga sotib olishingizni kiriting✍🏻 (Faqat raqam⚠)"))
	chegirma_miqdor = chegirma * (5/100)
	yakuniy_narx = chegirma - chegirma_miqdor
	print(f"Agar siz bu paketni xarid qilsangiz bu paket sizga {yakuniy_narx} - so'mga to'shadi(5% chegirmasi bilan.)")
	olmoq = input("Siz bu paketni sotib olasizmi? ")
	if olmoq not in ["ha", "Ha","H","h","olaman"]:
		print("Bizning xizmatdan foydalanganiz uchun rahmat☺")
		print("Xayr salomat bo'ling🤝🏻")
	else:
		print("Ajoyib👍🏻.Juda yaxshi tanlov qilingiz💰")
		tulov = input("To'lovni naxt qilasizmi yoki kartada?💳 ")
		if tulov in ["Naxd", "Naxt", "Naqd", "Naxd pul", "Naxt pul", "Naqd pul", "naxt", "naqd", "naxd"]:
			print("Hozirda Naxt pul uchun to'lov kasamiz mavjud emas ❌. Buning uchun uzr so'raymiz🙁")
		elif tulov in ["Kartada", "Karta","karta", "Bank karta", "kartada"]: 
			print("Juda yaxshi tanlov✔")
			print("Bizda hozicha 'Humo', 'Agrobank' va 'Uzkard' kartalari qabul qilinadi✅")
			karta = int(input("kartangizni kiriting💳: "))
			amal = input("Amal qilish muddati: ")
			kim_nomida = input("Kimning nomida✍🏻: ")
			print("Ajoyib🥳. sizning xaridingiz tasdiqlandi✔")

		else:
			print("To'g'ri yozing⚠")
elif xarid_summasi > 100000 and xarid_summasi <= 150000:
	print("Juda yaxshi🤗. Siz to'g'ri yuldasiz✅ ")
	print(paket_100)
	chegirma1 = int(input("Aynan qanchaga sotib olishingizni kiriting✍🏻 (Faqat raqam⚠) "))
	chegirma_miqdor2 = chegirma1 * (10/100)
	yakuniy_narx1 = chegirma1 - chegirma_miqdor2
	print(f"Agar siz bu paketni xarid qilsangiz bu paket sizga {yakuniy_narx1} - so'mga to'shadi(10% chegirmasi bilan.)")
	olmoq = input("Siz bu paketni sotib olasizmi? ")
	if olmoq not in ["ha", "Ha","H","h","olaman"]:
		print("Bizning xizmatdan foydalanganiz uchun rahmat☺")
		print("Xayr salomat bo'ling🤝🏻")
	else:
		print("Ajoyib👍🏻.Juda yaxshi tanlov qilingiz💰")
		tulov = input("To'lovni naxt qilasizmi yoki kartada?💳 ")
		if tulov in ["Naxd", "Naxt", "Naqd", "Naxd pul", "Naxt pul", "Naqd pul", "naxt", "naqd", "naxd"]:
			print("Hozirda Naxt pul uchun to'lov kasamiz mavjud emas ❌. Buning uchun uzr so'raymiz🙁")
		elif tulov in ["Kartada", "Karta","karta", "Bank karta", "kartada"]: 
			print("Juda yaxshi tanlov✔")
			print("Bizda hozicha 'Humo', 'Agrobank' va 'Uzkard' kartalari qabul qilinadi✅")
			karta = int(input("kartangizni kiriting💳: "))
			amal = input("Amal qilish muddati: ")
			kim_nomida = input("Kimning nomida✍🏻: ")
			print("Ajoyib🥳. sizning xaridingiz tasdiqlandi✔")
		else:
			print("To'g'ri yozing⚠")
else:
	print("Bunday narxda paketlar mavjud emas❌")

keying2 = """

       Keyingisi →

"""
print(keying2)


# 3.kirish qismi:

logins = ["Admn1234", "admin1234", "admin"]
parols = ["123456789", "admin1", "admin", "admin1234"]

print("Assalomu aleykum🤗. Qurbonalining dasturiga xush kelibsiz😎")
print("Admin panelidan foydalanish uchun login parolingizni kiritishingiz zarur⚠")
login = input("Loginingiz: ")
parol = input("Parolingiz: ")

if login in logins and parol in parols:
	print("Dasturga xush kelibsiz🤗")
else:
	print("Login yoki Parol xato❌")

keying3 = """

       Keyingisi →

"""
print(keying3)


# 4. Film Yosh Cheklovi:

films = """

Bizda bor filimlar: 

1. Qasoskorlar
2. Sherlok Holms
3. Superman
"""

print("Assalomu aleykum🤗. KinoTeatr dasturiga xush kelibsiz😎")
print("Bizning dasturdan foydalanishingiz uchun ro'yxatdan o'tishingiz lozim⚠")
print("_-_-_-_-_-_/Ro'yxatdan o'tish/_-_-_-_-_-_")
ism = input("Ismingiz: ")
familiya = input("Familiyangiz: ")
yosh = int(input("Yoshingiz: "))
if yosh < 13 :
	print("Sizga ushbu filmlar tavsiya etilmaydi❌")
  
elif yosh > 13 and yosh < 17:
	print("Siz filmlarni ota-onangiz bilan ko'rishingiz mumkin✔")
elif yosh >= 18 :
	print("Siz filmlarni tomosha qilishingiz mumkin✅")

print("Bizda hozircha shu filimlar mavjud⬇: ")
print(films)
choice = input("Qaysi birini tanlaysiz? ")
if yosh > 13 and choice in ["1", "Qasoskorlar", "qasoskorlar" ]:
	print("Qasoskorlar⁉🤯. Ajoyib tanlov👍🏻")
	print("Marhamat tomosha qiling🤗") 
elif choice in ["2","Sherlok Holms","sherlok Holms" ]:
	print("Detektiv bo'lmoqchimisiz shekeli? ")
	print("Marhamat tomosha qiling🤗") 
elif choice in ["3", "Superman", "superman"]:
	print("Fantastik janr. Juda yaxshi qaror🤝🏻")
	print("Marhamat tomosha qiling🤗") 
else:
	print("Bunday film hali mavjud emas❌")


keying4 = """

       Keyingisi →

"""
print(keying4)

# 5.Restoran Menyusi:
menyu = """

         Ergashev | Qurbonali Restauranti.

                      Menyu:
1. Osh
2. Mastava 
3. Shashlik
 

"""
tarif_osh = """

         Ergashev | Qurbonali Restauranti.

                      Tarif:
1. 50 ming -  so'mli.
2. 100 ming - so'mli
3. 150 ming - so'mli
"""
tarif1 = ["1.", "50 ming", "50 mingli", "50", "50 ming -  so'mli", "1. 50 ming -  so'mli.","50mingli"]
tarif2 = ["2", "100 ming", "100", "100ming", "100 mingli", "2. 100 ming - so'mli","100 ming - so'mli"]
tarif3 = ["3", "150", "150ming","150 ming", "150 mingli","3. 150 ming - so'mli","150 ming - so'mli"] 

print("Assalomu aleykum🤗. Bizning restorantga xush kelibsiz🙂")
print(f"Bizning restorantda shu taomlarni topishingiz mumkin✔: {menyu}")
choice = input("Qaysi taomni iste'mol qilmoqchisiz?  ")
if choice in ["1", "Osh", "osh"]:
	print("Ajoyib tanlov😊")
	tarif_surash = input(f"Osh taxminan 2-soatda tayyor bo'ladi✔. Va bizda 3 xil ta'rif mavjud qaysi birini tanlaysiz?  Tariflar⬇: {tarif_osh}")
	# print(f"Tariflar⬇: {tarif_osh}")
	if tarif_surash in tarif1:
		print("Yaxshi tanlov. Sizning buyurtmangiz 2-soatda tayyor bo'ladi✔")
	elif tarif_surash in tarif2:
		print("Juda yaxshi va qimmatli tanlov🤩. Sizning 100ming so'mli oshingiz taxminan 2-soatda tayyor bo'ladi✔")
	elif tarif_surash in tarif3:
		print("Juda yaxshi tanlov qildingiz boy aka🤑.Sizning 150 mingli oshingiz 2-soatda tayyor bo'ladi✔ ")
	else:
		while tarif_surash not in tarif1 :
			print("Iltimos, to'g'ri yozing⚠")
			tarif_surash = input(f"Qaysi birini tanlaysiz?  Tariflar⬇: {tarif_osh}")
		while tarif_surash not in tarif2 :
			print("Iltimos, to'g'ri yozing⚠")
			tarif_surash = input(f"Qaysi birini tanlaysiz?  Tariflar⬇: {tarif_osh}")
		while tarif_surash not in tarif3 :
			print("Iltimos, to'g'ri yozing⚠")
			tarif_surash = input(f"Qaysi birini tanlaysiz?  Tariflar⬇: {tarif_osh}")

elif choice in ["2","Mastava","mastava","2.mastava","2.Mastava","M","m"]:
	print("Yaxshi tanlov😊. Bizda hozir faqat bitta tarif mavjuda yane 30 mingli tarifimiz bor.")
	answer = input("Taomni tasdiqlaysizmi? ")
	if answer in ["ha","Ha","h","Albatta","H","HA"]:
		print("Tanlovingiz uchun rahmat😊. Sizning taomingiz 1-soatda tayyor bo'ladi✔")
	else:
		print("Iltimos, to'g'ri yozing⚠")
elif choice in ["Shashlik","shashlik","3.shashlik","3.Shashlik","Sh","sh","3"]:
	print("Yaxshi tanlov😊. Bizda hozir faqat bitta tarif mavjuda yane 20 mingli tarifimiz bor.")
	answer = input("Taomni tasdiqlaysizmi? ")
	if answer in ["ha","Ha","h","Albatta","H","HA"]:
		print("Tanlovingiz uchun rahmat😊. Sizning taomingiz 1-soatda tayyor bo'ladi✔")
	else:
		print("Iltimos, to'g'ri yozing⚠")

elif choice in ["Shashlik","shashlik","3.shashlik","3.Shashlik","Sh","sh","3"]:
	print("Yaxshi tanlov😊. Bizda hozir faqat bitta tarif mavjuda yane 20 mingli tarifimiz bor.")
	answer = input("Taomni tasdiqlaysizmi? ")
	if answer in ["ha","Ha","h","Albatta","H","HA"]:
		print("Tanlovingiz uchun rahmat😊. Sizning taomingiz 1-soatda tayyor bo'ladi✔")
	else:
		print("Iltimos, to'g'ri yozing⚠")
else:
	while choice != True: 
		print("Iltimos, to'g'ri yozing⚠")
		choice = input("Qaysi taomni iste'mol qilmoqchisiz? ")



keying5 = """

       Keyingisi →

"""
print(keying5)


# 6. Email Tekshiruvi:
print("Assalomu aleykum. Bizga o'z fikringizni yozishingiz uchun emailingizni yozishingiz shart⚠")
fikr = input("Fikringizni yozing: ")
email = input("Emailingiz: ")
if email.find("@") == -1 and email.find("gmail.com") == -1:
	print("Emailingiz Xato❌.")
	print("Emailda '@'va 'gamail.com' bo'lishi shart⚠")
	while email.find("@") == -1 and email.find("gmail.com"):
		email = input("Emailingiz: ")

else:
	print("Emailingiz Qabul qilindi✔")
	print("Sizning fikringiz Muvaffaqiyatli yuborildi✅")
	


keying6 = """

       Keyingisi →

"""
print(keying6)


# 7. Talaba Baholash Tizimi: 

print("Kundalik comga xush kelibsiz!")
print("Siz qaysi fandan nechi ball olganingizni aytsangiz men sizga bahoyingizni aytaman✍🏻")
print("Qaysi fanndan nechi ball olganingizni ayting⁉")
fan = input("Fan nomini  yozing✍🏻:  ")
ball = int(input("Nechi ball oldingiz (faqat raqam) : "))
if ball <55 and ball>0:
	print(f"Siz {fan} - dan 2 baho olibsiz🙁")
elif ball>55 and ball<69:
	print(f"Siz {fan} - dan 3 baho olibsiz😔")
	print(f"Ammo xafa bo'lmang yanada yaxshiroq harakat qiling'✊🏻. Albatta yaxshi natijalarga erishasiz😉")
elif ball>70 and ball<85:
	print(f"Ajoyib siz {fan} - dan 4 bahoni qo'lga kiritibsiz😎")
	print("Harakat qilishdan to'xtamang😇")
elif ball>86 and ball<100:
	print(f"Barakala Sen bugun {fan} - dan 5 bahoga egalik qiliyapsan🤩")
	print("Bu juda yaxshi ammo hech qachon harakatdan to'xtamang👨🏻‍💻")
elif ball > 100 and ball < 1000:
	print("Tabriklayman siz proffesor darajasiga yetishibsiz🙃")
elif ball>1000:
	print("Siz Mabodo Eshtein ikkinchi-masizku?😅")
elif ball<-1:
	print("Siz o'zi maktabda o'qiyapsizmi?😐")
else:
	print("To'g'ri yozing✍🏻")


keying7 = """

       Keyingisi →

"""
print(keying7)


# 8.Bankomat Pul Yechish:

print("Bankomatga xush kelibsiz😅")
bank_karta = input("Bank kartangizni raqamini kiriting (masalan: 8600 1234 5678 9012):  ")
while len(bank_karta) != 19:
	print("Kartangiz xato❌") 
	bank_karta = input("Iltimos, bank kartangizni to'g'ri formatda kiriting: ")

print("Karta muvaffaqiyatli qabul qilindi ✅\n")
bank_karta_mablag = input("Kartangizda qancha pul bor? ")
while not bank_karta_mablag.isdigit():
	print("Xato faqat raqam kiriting! ")
	bank_karta_mablag = input("Kartangizda qancha pul bor? ")

print("Mabilag' muvaffaqiyatli tasdiqlandi ✔\n")

bank_karta_yechish = input("kartangizdan qancha pul yechib olmoqchisiz? ")
while not bank_karta_yechish.isdigit():
	print("Xato faqat raqam kiriting! ")
	bank_karta_yechish = input("kartangizdan qancha pul yechib olmoqchisiz? ")


bank_karta_mablag = int(bank_karta_mablag)
bank_karta_yechish = int(bank_karta_yechish)

confirm = input("Ishonchingiz komilmi? ")
if confirm in ["Ha", "ha","HA","Albatta","h","H"]:
	if bank_karta_mablag - bank_karta_yechish < 5000:
		print("Mabilag'izda pul yetarli emas❎\n")
	else:
		bank_karta_qolganpul = bank_karta_mablag - bank_karta_yechish
		bank_karta_qolganpul2 = bank_karta_qolganpul - 2000
		print(f"Hisobingizdan {bank_karta_yechish} - miqdorda pul yechib olindi✔\n")
		print(f"Sizning kartangizda {bank_karta_qolganpul2} - miqdorda pul qoldi (2000-ming so'm xizmat haqi olindi✔\n)")
else:
	print("Jarayon to'xtadildi❌\n")


keying8 = """

       Keyingisi →

"""
print(keying8)


# 9. Ish Jadvalini Tekshirish: 

print("Men ish jadvalini tekshiradigan robot🤖 man.")
kun = input("Bugun Qaysi kun? ")
if kun.lower() in ["dushanba", "seshanba", "chorshanba","payshanba","juma"]:
	print("Bugun ish kuni👷🏻‍")
	print("Ishlaringizga omad☺")
elif kun.lower() in ["shanba","yakshanba"]:
	print("Bugun dam olish kuni😇")
	print("Maroqli hordiq tilayman😊")
else:
	print("Bunday hafta kuni mavjud emas❌\n yoki to'g'ri yozing✔\n")


keying9 = """

       Keyingisi →

"""
print(keying9)


# 10. Mobil Tarif Tanlash:


print("Men sizga qaysi tarifdan foydalanishingizni aytadian dasturman🤖\n")
Tarif = int(input("Oyiga nechi GB(Gigabayt) ishlatasiz? "))
if Tarif < 1:
	print("Siz 'mini' tarifdan foydalanar ekansiz✔\n")
elif Tarif > 1 and Tarif <= 5:
	print("Siz 'standart' tarifdan foydalanar ekansiz✔\n")
elif Tarif > 5:
	print("Siz 'Unlimited' tarifdan foydalanar ekansiz✔\n")
else:
	print("Xato❌. Iltimos, faqat raqam yozing;⚠\n")
	# pass

tugadi = """

       Tamom 🔚

"""
print(tugadi)
