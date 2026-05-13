# # -_-_-_-_-_-_-_-_-_-_-For Sikli-_-_-_-_-_-_-_-_-_-_-


# # 0.5 Qiziqishlar:

# print("Bizning dasturga xush kelibsiz🤗")
# print("_"*20)
# qiziqish = input("Nimaga qiziqasiz?  ")
# print("_"*40)


# if qiziqish.find("kitob") >= 0 or qiziqish.find("kutubxona") >= 0:
# 	qiziqish_kitob = input("Qanday kitoblarga qiziqasiz?📕 ")
# 	print("_"*40)
# 	if qiziqish_kitob.find("detektiv") >= 0 :
# 		shaytanat = input("Sizningcha Shaytanat qanday kitob?📜 ")
# 		print("_"*40)

# 		print("Juda yaxshi☺. Kitob o'qishdan hech qachon to'xtamang⚠")
# 		print("_"*40)
# 	if qiziqish_kitob.find("diniy") >= 0:
# 		print("Juda yaxshi tanlov✔. Sizga diniy kitoblarga qiziqishingiz sababali 'Hadis va Hayot' kitobni sovg'a qilamiz🎁")
# 		print("_"*40)

	

# else:
# 		pass
# 		print("_"*40)



# if qiziqish.find("sport") >= 0:
# 	print("Juda yaxshi👍🏻")
# 	print("_"*40)

# 	choose = input("Aynan Sportning qaysi turiga qiziqasiz?")
# 	print("_"*40)

# 	if choose.find("futbol") >= 0:
# 		type = input("Futbol⚽️. Juda zo'r💪🏻. Qaysi komandani ishtiyoqmandisiz? ")
# 		print("_"*40)
# 		if type.find("barsa") >= 0 or type.find("real") >= 0:
# 			print("Ajoyib🤩. Sizga biz el-classicoga chiptasini sovg'a qilamiz🎁")
# 			print("_"*40)

	
# else:
# 		print("Yaxshi, qiziqishlaringizni hech qachon yo'qotmang.")


# print("| ^_^ | " * 12)


# # 1.  Elektron Pochta Manzillarini Tekshirish:


# Emails = ["abcdgmail.com", "abcd1@yahoo.com","abcd9@outlook.com"]
# for email in Emails:
# 	if "@" not in email:
# 		print(f" {email} -- XATO❌")
		
# 	else:
# 		print(f"{email} -- TO'GRI✔")


# keying = """

#        Keyingisi →

# """
# print(keying)

# # 2.Parol Kuchini Tekshirish:

# belgilar = "!@$#%&*~"

# paswords  = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# for pasword in paswords:
# 	if len(pasword) < 8 :
# 		print(f"{pasword}--Parol juda qisqa🛅")

# 	elif not any (belgi in pasword for belgi in belgilar):
# 		print(f"{pasword}--Parol juda kuchsiz🪫")
# 	else:
# 		print(f"{pasword}--Juda kuchli parol🦾")


# keying2 = """

#        Keyingisi →

# """
# print(keying2)


# # 3.Ob-havo Ma'lumotlarini Tahlil Qilish:

# degrees = [20, 22, 19, 24, 25, 23, 21]
# overal_deg = 0

# print("Kunlik hisobot: ")
# print("_" * 20)


# for degree in degrees:
# 	overal_deg += degree
# 	if degree > 22 :
# 		print(f"{degree}℃:  iliq kun.")
# 	else:
# 		print(f"{degree}℃:  salqin kun.")

# ortacha = overal_deg / len(degrees)
# print("_" * 20)
# print(f"Haftalik o'rtacha harorat : {ortacha}℃ ")




# keying3 = """

#        Keyingisi →

# """
# print(keying3)


# # 4. Restoran Buyurtmalari:

# foods = ["Osh", "Shashlik", "Manti", "Lag’mon"]

# print("Bizning restorantga xush kelibsiz🤗 ")
# book = input("Nima bo'yirasiz?📝  ")

# for food in foods:
# 	if book.title() not in foods:
# 		print("Kechirasz, ammo bunday taom bizning restorantda mavjud emas❌\n")
# 	else: 
# 		print("Buyurtmangiz qabul qilindi✔\n")
# 		print("Buyurtmangiz 1-1.30 soatlarda tayyor bo'ladi✅\n")

# 	break




# keying4 = """

#        Keyingisi →

# """
# print(keying4)


# # 5. Anketa Tahlili:

# ages = [16 , 21 , 17, 30, 25]

# for age in ages:
# 	print("Natija: ")
# 	print("(●'◡'●)" * 10)
# 	if age < 18:
# 		print("_"*40)
# 		print(f"{age}-yosh -- Sizning yoshingiz yetmaydi!❌\n ")
# 		print("_"*40)
# 	elif age > 18:

# 		print(f"{age}-yosh -- Dasturga xush kelibsiz🤗")
# 		print("_"*40)



# keying5 = """

#        Keyingisi →

# """
# print(keying5)


# # 6. Mobil Ilova Bildirishnomalari:

# messages = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]

# for message in messages:
# 	if message == "Batareya past":
# 		print(f"Telefoningizni quvvatlang🔋")
# 		print("~"*25)
# 	elif message == "Yangi xabar":
# 		print("Sizda yangi xabar bor🆕 ")
# 		print("~"*25)
# 	elif message == "Yangilanish mavjud":
# 		print("Telefoningizni yangilang🔄")
# 		print("~"*25)
	


# keying6 = """

#        Keyingisi →

# """
# print(keying6)


# # 7. Fayllarni guruhlash:

# files =  [ "kitob.jpg", "ko_ jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
# songs = []
# images = []

# for file in files:
# 	if file.endswith(".mp3"):   
# 		songs.append(file)

# 	if file.endswith(".jpg"):
# 		images.append(file)

# print(f"Musiqalar tuplami: {songs}")
# print(f"Rasmlar tuplami: {images}")	


# tugadi = """

#        Tamom 🔚

# """
# print(tugadi)





x = 1
while False:
    x = x + 1
print(x)