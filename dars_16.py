# Imports: 
from collections import Counter



# 1.Counter
# javob = {}
# def str_counter(strs):
# 	for i  in strs:
# 		a = len(i)
# 		javob[a] = i
# 	return javob

# salom = ["nok", "behi", "shaftoli"]
# print(str_counter(salom))


# 2. Dict

# def merge_list(l1,l2):
# 	my_dict = {}
# 	for i in range(len(l1)):
# 		my_dict[l1[i]] = l2[i]
# 	return my_dict

# list_1 = ["a", "b", "c"] 
# list_2 = [1, 2, 3]
# print(merge_list(list_1, list_2))


# 3.dict

# def qoshish():
# 	if tanlang.lower() in ["1", "yangi kontakt yaratish", "yangi kontakt", "kontakt yaratish"]:
# 		print("_"*38)
# 		name = input("F.I.SH (Familiya, Ism, Sharif) yozing: ")
# 		print("_"*25)
# 		tel = input("Telefon raqamni kiriting: ")
# 		print("_"*80)
# 		while tel.find("+998") == -1:
# 			print("_"*30)
# 			print("To'g'ri formatda yozing!(Faqat Uzbekiston davlatiga tegishli bo'lgan Telefon raqam kiriting! (+998))")
# 			print("_"*30)
# 			tel = input("Telefon raqamni kiriting: ")

# 		contacts[name] = tel
# 		print("="*90)
# 		print(f"Natija: {contacts}") 
# 		print("="*90)
	
# def yangilash():
# 	if tanlang.lower() in ["2","yangilash","2.Yangilash"]:
# 		print("="*90)
# 		print(f"Mavjud kontaktlar: {contacts}")
# 		print("="*90)
# 		entering_news = input("Qaysi Kontaktni yangilashni ya'ne uzgartirishni xoxlaysiz? ")
# 		print("_"*65)
# 		if entering_news.lower() in ["nodir", "laziz"]:
# 			deleted_contact = contacts.pop(entering_news.capitalize())
# 			yangi_nom = input("Yangilamaoqchi bo'lgan kontaktingizni ismni yozing: ")
# 			print("_"*60)
# 			yangi_tel = input("Tel: ")
# 			print("_"*15)
# 			contacts.update({yangi_nom: yangi_tel})
# 			print("="*90)
# 			print(f"Kontaktlar muvaffaqiyatli yangilandi:  {contacts}")
# 			print("="*90)
# 		else:
# 			print("Bunday foydalanuvchi mavjud emas!")

# def uchirish():
# 	if tanlang.lower() in ["3", "o'chirish", "ochirish"]:
# 		print("_"*85)
# 		delete = input(f"Qaysi Kontaktni o'chirmoqchisiz? {contacts}")
# 		print("_"*85)
# 		if delete.capitalize() in contacts:
# 			# contacts.pop(delete.capitalize())
# 			del contacts[delete.capitalize()]
# 			print("="*60)
# 			print(f"Kontakt muvaffaqiyatli uchirildi. Qolgan kontaktlar: {contacts}")
# 			print("="*60)
# 		else:
# 			print("Bunday foydalanuvchi mavjud emas!")
			
# 	else:
# 		pass


# def qidirish():
# 	if tanlang.lower() in ["4", "qidirish", "4.qidirish"]:
# 		print("_"*45)
# 		poisk = input("Kontaklardan qaysi kontakni qidirmoqchisiz? ")
# 		print("_"*45)
# 		if poisk in contacts:
# 			print("="*30)
# 			print("Kontakt muvaffaqiyatli topildi.")
# 			print("="*30)
# 			print(f"Natija: {poisk} : {contacts.get(poisk, "Kechirasiz, bunday kontakt mavjud emas")}")
# 			print("="*30)
# 		else: 
# 			print("Kechirasiz, bunday kontakt mavjud emas")
# 			print("_"*45)


	


# contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"} 
# while True:
# 	print("Assalomu aleykum, Kontaklar dasturiga xush kelibsiz")
# 	print("Siz bu dastur orqali yangi kontakt yaratish, yangilash, uchirish va qidirishingiz mumkin. ")
# 	print("""
# 	╔══════════════════════════════════════════╗
# 	║             KONTAKTLAR MENU              ║
# 	╠══════════════════════════════════════════╣
# 	║                                          ║
# 	║   [1] ➕ Yangi kontakt yaratish          ║
# 	║   [2] 🔄 Mavjud kontakni yangilash       ║
# 	║   [3] 🗑️ Kontaktni o'chirish             ║
# 	║   [4] 🔍 Kontaktni qidirish              ║
# 	║   [0] ❌ Dasturdan chiqish               ║
# 	║                                          ║
# 	╚══════════════════════════════════════════╝

# 	""")

# 	tanlang = input(f"➢ Tanlovingizni kiriting: _ ")

# 	qoshish()
# 	yangilash()
# 	uchirish()
# 	qidirish()
# 	if tanlang.lower() in ["0", "chiqish", "dasturdan chiqish"]:
# 		print("~"*30)
# 		print("Dastur to'xtatildi!")
# 		print("~"*30)
# 		break



# 4. Dict


# numbers = [1,2,3,4,5,6,1,2,3,4,56,2,2,5,6,5,8,111]
# def counter_dict(nums):
# 	count = Counter(nums)
# 	return ( dict(count))

# print(counter_dict(numbers))


# 5. Dict
# def balni_ol(juftlik):
# 	return juftlik[1]

# def max_ball_students(talabalar):
# 	talaba = sorted(talabalar.items(), key=balni_ol, reverse=True)
# 	yaxshi_talabalar = talaba[:2]
# 	student = dict(yaxshi_talabalar)
# 	return student

# students = {"Ali": 52, "Vali": 45, "Akmal": 51, "Anvar": 58}

# natija = max_ball_students(students)


# print("\n" + "="*30)
# print("🏆  ENG YAXSHI TALABALAR  🏆")
# print("="*30)

# for ism, ball in natija.items():
#     print(f"👤 Ism :{ism:<10} | ⭐️ Ball: {ball}")

# print("="*30)
# print(f"Jami saralangan: {len(natija)} ta")
# print("="*30 + "\n")

