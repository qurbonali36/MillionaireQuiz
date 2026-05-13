# __--__--__--__--__--__--__--__While sikli(loop)__--__--__--__--__--__--__--__


import random
# 1.Svetafor:

# print("Assalomu aleykum😊")
# svetafor = input("Svetafor qanday rangda?🚦  ")
# colors = ["qizil", "yashil", "sariq"]
# while svetafor.lower() in colors:
# 	print(f"Ajoyib👍🏻, Hozir Svetafor: {svetafor} - Rangda ekan😎")
# 	break

# else:
# 	print("Xato ❌, Qaytadan urinib ko'ring🔁")


# 2.  Tasodifiy Sonni Topish O'yini:

# tasodifiy_son = random.randint(1,10)
# max_urinishlar = 5
# urinishlar = 0

# print(f"Men 1-10 bo'lgan sonni o'ylaydim. Siz u raqamni topishingiz lozim?🔎. Sizda {max_urinishlar}  -- urinish bor⚠ ")

# while urinishlar < max_urinishlar:
# 	son_user = int(input(f"Sonni kiriting: "))

# 	urinishlar += 1
	
# 	if son_user == tasodifiy_son:
# 		print("To'g'ri! ✔ Siz yutdingiz🥳")
# 		break

# 	elif son_user < tasodifiy_son:
# 		print("Xato❌ — o'ylagan son bundan kattaroq. 🔼")
# 	else:
# 		print("Xato❌ — o'ylagan son bundan kichikroq. 🔽")

# 	print(f"Qolgan urinishlar: {max_urinishlar - urinishlar}")
	

	
# 	if son_user < 1 or son_user > 10:
# 		print("Son 1 dan 10 gacha bo'lishi kerak⚠")
# 		continue

	

# if urinishlar >= max_urinishlar and son_user != tasodifiy_son:
# 	print("Uzr, siz barcha urinishlardan foydalanib bo'ldingiz!🔚")
# 	print(f"To'g'ri javob: {tasodifiy_son}")





# 3.Do'stlar Ro'yxatini Yaratish:

# dost_ruyxati = []
# print("Assalomu aleykum👋. Bu dasturda siz do'stlaringizni ismlarini qo'shasiz➕. ('stop' deb yubormaguningizgacha dastur to'xtamaydi⚠)")

# while True:
# 	dost_nomi = input("Do'stingizni  nomini kiritng: ")

# 	if  dost_nomi.lower() == "stop":
# 		print("Jarayo to'xtatildi❌")
		
# 		print(f"Siz kiritgan do'stlaringiz: {dost_ruyxati}")
# 		break
# 	else:
# 		dost_ruyxati.append(dost_nomi)
# 		print(f"Sizning do'stlaringizni ro'yxati: {dost_ruyxati}")


# 4.  Valyuta Ayirboshlash Kalkulyatori: 

# usd = 12600 #sum
# print("Men valyuta hisob kitob qiladigan dasturman🤖")
# print("-" * 40)
# print("Men sizga Dollardan so'mga utkazib beraman💹")
# print("-" * 40)
# print("Valyutani uzgartirish uchun 'uzgartirish' - deb yozing❗")
# print("=" * 40)
# print("'exit' - yozmagunizgacha men to'xtamayman❌")
# print("=" * 40)
# while True:
# 	print("_" * 40)
# 	budjet = input("Sizda Qancha pul bor❓(Dollar💵-DA kiriting❗) \n")
# 	print("_" * 40)
# 	if budjet.lower() == 'exit':
# 		print("<x>" * 10)
# 		print("Jarayon to'xtatildi❌")
# 		print("<x>" * 10)
# 		break

# 	if budjet.lower() == "uzgartirish":
# 		print("=" * 40)
# 		print("Valyuta Muvaffaqiyatli uzgartirildi✔")
# 		print("=" * 40)
# 		budjet = input("Sizda Qancha pul bor❓(So'm💸-DA kiriting❗) ")
# 		print("-" * 40)
# 		budjet = float(budjet)
# 		pul = budjet / usd
# 		print("_" * 40)
# 		print(f"{budjet:,} so'm {pul:,.0f} dollar bo'ladi😄")

# 	budjet = float(budjet)
# 	if budjet > 1000000000000:
		
# 		print("Bunday katta summa tizimda ishlanmaydi!\n")
# 	else:
# 		budjet = float(budjet)
# 		pul = usd * budjet
# 		print(f"{budjet:,} dollar {pul:,.0f} so'm bo'ladi\n") 

	
# 5.while sikli
# number = 1 #1-usul
# while number <= 5:
# 	print(str(number)*number)
# 	number += 1
# 2-usul:
# while number <= 5:
# 	num = 1

# 	while num <= number:
# 		print(number, end=" ")
# 		num += 1

# 	print(" ")
# 	number += 1


# 6. while sikli

# a = input("Raqam kiriting: ")
# k = 0
# a = int(a)
# while a > 0:
# 	b = a % 10
# 	print(b)
# 	k = k + b 
# 	a = a // 10


	

# print(k)



# 7.While sikli:

# a = 99
# yigindi = 0

# while a > 0 :
# 	yigindi = a + yigindi
# 	a  = a - 2

	


# print(f"{yigindi} - yig'indi.")
	
	
# 8.While sikli

 #     