import colorama
from colorama import Fore, Style, Back
colorama.init(autoreset=True)

1

# class Easy1:
# 	a = 18
# 	def output_a(self):
# 		print(self.a)


# raqam = Easy1()
# raqam.output_a()


2.

# class Easy2:
# 	a = 25
# 	b = 90
# 	def summa(self):
# 		print(self.a + self.b)
# 		# qushish = sum([self.a, self.b])
# 		# print(qushish)

# yigindi = Easy2()
# yigindi.summa()

3.

# class Easy3:
# 	def plus_minus(self, a):
# 		self.a = a 
# 		if int(a) > 0:
# 			print("Bu musbat son!")
# 		elif int(a) == 0:
# 			print("Bu sifr!")
# 		else:
# 			print("Bu manfiy son!")

# a = input("A = ")
# klass = Easy3()
# klass.plus_minus(a)


4. 

# class Easy4:
# 	def odd_even(self, b):
# 		self.b = b
# 		if int(b) == 0:
# 			print("Bu sifr!")
# 		elif int(b) % 2 == 0:
# 			print("Bu juft son!")
# 		elif int(b) < 0:
# 			print("Bu manfiy son!")
# 		elif int(b) %2 != 0:
# 			print("Bu toq son!")
		

# b = input("B = ")
# odd = Easy4()
# odd.odd_even(b)


5.

# class Easy5:
# 	def daraja(self, a, b):
# 		self.a = a
# 		self.b = b
# 		daraja2 = int(a) ** int(b)
# 		daraja3 = pow(a,b)

# 		print(f"{a} - ning {b}-chi darajasi = {daraja2}")

# try:
# 	a = int(input(" A = "))
# 	b = int(input(" B (A ning drajasi) = "))
# 	daraj = Easy5()
# 	daraj.daraja(a,b)
# except ValueError :
# 	print("Faqat raqam kiriting!")


6. 

# class MyClass6:
# 	words = []
# 	def add_word(self,  word):
# 		self.word = word
# 		self.words.append(word)
# 		return self.words

# 	def remove(self, word):
# 		self.word = word
# 		self.words.remove(word)
# 		return self.words

# suz = input("So'z yozing: ")
# klas = MyClass6()
# print(klas.add_word(suz))
# print(klas.remove(suz))



7.

# class MyClass7:
# 	myDict = {}
# 	def add_elem(self, key, val):
# 		self.key = key
# 		self.val = val
# 		if self.myDict.keys() != key:
# 			self.myDict["ism"] = key
# 			self.myDict["yosh"] = val
# 			# print(self.myDict)
# 		else:
# 			pass
#
# 	def update_elem(self, key, val):
# 		self.key = key
# 		self.val = val
# 		if self.myDict[key] == key:
# 			self.myDict[key] = val
# 		else:
# 			print(f"{Fore.RED}Xatolik❌")
# 	def see(self):
#
# 		print( "="*50)
# 		print(" 📋Mehmonlar Ro'yxati")
# 		print("="*50)
# 		bosh_qism = f"{'Ism':<15} |     {'Yosh':<15}"
# 		print(f"{Fore.BLACK}{Back.WHITE}{bosh_qism}")
# 		if not self.myDict:
# 			print("\n",{Fore.RED + Style.BRIGHT},"      Ro'yxat bo'sh    ")
# 		else:
# 			print(f"{self.myDict["ism"]: <15} |     {self.myDict["yosh"]: <15}")
# 			print("="*50)
# while True:
# 	menyu = input(f"""
# 	{Fore.CYAN}1 - ➕Ma'lumot qo'shish
# 	2 - 📝Ma'lumot yangilash
# 	3 - 👀Ma'lumot ko'rish
# 	{Fore.RED}0 - 🛑 Chiqish
# 	""")
# 	if menyu == "1":
# 		try:
# 			ism = input("Ism: ")
# 			yosh = int(input("Yosh: "))
# 			if yosh > 100 or yosh <=0 or yosh == float:
# 				print("Yoshingizni to'g'ri kiriting!")
# 				continue
# 			else:
# 				Klass = MyClass7()
# 				Klass.add_elem(ism, yosh)
# 		except ValueError:
# 			print(f"{Fore.LIGHTRED_EX}Iltimos!, to'gri ma'lumot kiriting!")
# 			continue
#
# 	elif menyu == "2":
# 		try:
# 			ism = input("Ism: ")
# 			yosh = int(input("Yosh: "))
# 			if yosh > 100 or yosh <=0 or yosh == float:
# 				print("Yoshingizni to'g'ri kiriting!")
# 				continue
# 			else:
# 				Klass = MyClass7()
# 				Klass.update_elem(ism, yosh)
# 		except ValueError:
# 			print("Iltimos!, to'gri ma'lumot kiriting!")
# 			continue
# 	elif menyu ==  Klass = MyClass7"3":
# #()
# 		Klass.see()
# 	elif menyu == "0":
# 		print(f"{Fore.RED}{Back.LIGHTBLACK_EX}Dastur to'xtatildi❌")
# 		break


8.

# class MyClass8:
#     numbers = [1,5,8,6,7,8,5,8,5,599]
#     def compare_lists(self, new_list):
#         self.new_list = new_list
#         yigindi_l1 = sum(self.numbers)
#         yigindi_l2 = sum(new_list)
#         if yigindi_l1 > yigindi_l2:
#             print(f"{Fore.LIGHTMAGENTA_EX}Eng katta list: {Fore.LIGHTBLUE_EX}{self.numbers}")
#         else:
#             print(f"{Fore.GREEN}Eng katta list: {Fore.RED}{new_list}")
#
#
# Klas = MyClass8()
# Klas.compare_lists([5,54,8,6,8,8,5,998,5])

9.

# class MyClass9:
#     list1 = [1,2,300,4,8]
#     list2 = [100,200,3,5]
#     def list1_max(self):
#         cum = sum(self.list1)

#         return f"{Fore.GREEN}list 1-ning raqamlar yig'indisi: {cum}"

#     def list2_max(self):
#         cum2 = sum(self.list2)
#         return f"{Fore.RED}list 2-ning raqamlar yig'indisi: {cum2}"

#     def sum_of_two_max(self):
#         maxs_list = []
#         maks = max(self.list1)
#         maxs = max(self.list2)
#         maxs_list.append(maks)
#         maxs_list.append(maxs)
#         print(f"{Fore.BLACK}{Back.WHITE}Ikkita listning eng katta raqamlari: {maxs_list[0]},{maxs_list[1]}")
       
# klacc = MyClass9()
# klacc.sum_of_two_max()


10.

# class MyClass10:
#     numbers = [1,4,3,5,10,45,58,88,99,100]
#     def divide(self, d):
#         numbers_divide = []
#         no_divide = []
#         for n in self.numbers:
#             if n%d==0:
#                 numbers_divide.append(n)
#             elif n%d!=0:
#                 no_divide.append(n)

#         return f"{Fore.BLUE}{d}-ga bo'linadigan sonlar: {numbers_divide}\n{Fore.GREEN}{d}-ga bo'linmaydigan sonlar:  {no_divide}"


# clac = MyClass10()
# print(clac.divide(5))