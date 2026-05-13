import math
import random

 1.

class BankAccount:
	deposit2 = {"Deposit": 100}
	def deposit(self):
		try:
			name = input("✍️New deposit name: ")
			Depsit = int(input("How much money do you have in your deposit?(In Dollar💲) "))
			self.deposit2[name] = Depsit
			print(f"Your depsoit added: {self.deposit2}")
		except Exception as e:
			print(f"Please! Fill in the information correctly!⚠️ {e}")

	def  withdraw(self):
		try: 
			check = input("Which deposit do you want withdraw money? (Name)")
			if check in self.deposit2.keys():
				number = int(input("How  much do you want withdraw in your deposit?(Amount | in Dollar💲) "))
				# depo = self.deposit2[check]
				if number <= self.deposit2[check]:
					 withdrawing = self.deposit2[check] - number
					 self.deposit2[check] = withdrawing
					 print(f"Deposits: {self.deposit2}")
				else: 
					print("There is not enough money for withdrawing!⚠")
			else:
				print("Deposit in not defined")
		except Exception as e:
			print(f"Error: {e}")

	def check_balance(self):
		name = input("Which deposit do you want see?(Name) ").strip().capitalize()
		if name in self.deposit2.keys():
			print(f"Your depsoit: {self.deposit2}")
		else:
			print("No deposit has been opened with such a name!⚠")
		

bank = BankAccount()
# bank.deposit()
# bank.withdraw()
# bank.check_balance()

2.

class Rectangle:
	def __init__(self):
		self.length = 5
		self.width = 5
	def area(self):
		area = self.length * self.width
		return f"Area: {area}"
	def perimeter(self):
		perimeter2 = 2*(self.length + self.width)
		return f"Perimetr: {perimeter2}"
	def is_square(self):
		if self.length == self.width:
			return True
		elif self.length != self.width:
			return False
		else:
			None


rect = Rectangle()
# print(rect.area())
# print(rect.perimeter())
# print(rect.is_square())


3. 

class Student:
	def __init__(self):
		self.name = "Qurbonali"
		self.age = 16
		self.grades = [5,4,5,4,5,5,5,5,5]

	def add_grade(self):
		try:
			add = int(input("Bahoni kiriting(Faqat raqam): "))
			self.grades.append(add)
			print(f"Baholar: {self.grades}")
		except ValueError:
			print("Iltimos! Faqat raqam kiriting!⚠")


	def calculate_average(self):
		everage = 0
		for grade in self.grades:
			everage += grade
		everage_grade = everage/len(self.grades)
		if everage_grade % int(everage_grade) >= 0.5:
			everage_grade = int(everage_grade) + 1
			print(f"O'rtacha baho: {everage_grade}")
		elif everage_grade % int(everage_grade) < 5:
			print(f"O'rtacha baho: {int(everage_grade)}")


	def print_summary(self):
		print("="*45)
		print(f"{"📋Talaba haqida mal'umot":^44}")
		print("="*45)
		print(f"{"👤Ism":^18}", f"{"📈Yosh\n" :^27}")
		print(f"{self.name:^23}",f" {self.age:^19}")
		print("="*45)
		print(f"{"🧾Baholar:":^44}")
		print(f"{"":>8}{self.grades}")
		print("="*45)


stud = Student()
# stud.add_grade()
# stud.calculate_average()
# stud.print_summary()


4.


class Circle:
	def __init__(self, R):
		self.R = R
	def area(self):
		area2 = math.pi * (self.R**2)
		print(f"Area: {round(area2, 2)}")

	def circumference(self):
		circumference2 = 2 * (math.pi * self.R)
		print(f"Aylana uzunligi: {round(circumference2,2)}")

	def diameter(self):
		diameter2 = 2 * self.R
		print(f"Diametr: {round(diameter2, 2)}")



# print("="*45)
# R = float(input("Radiusni kiriting: "))		
# print("="*45)
# circle = Circle(R)
# print("="*45)
# circle.area()
# print("="*45)
# circle.circumference()
# print("="*45)
# circle.diameter()
# print("="*45)


5.
 

class Book:
	def __init__(self):
		self.title = "Margi Sudxur"
		self.author = "Sadridin Ayni"
		self.current_page = 1

	def open(self):
		print("Bu random book bo'lib, sizni tasodidify sahifaga o'tkazadi.")
		print(f"Siz turgan sahifa (Oldin): {self.current_page}")
		self.current_page = random.randint(2,196)
		print(f"Siz hozir turgan sahifa: {self.current_page}")

	def turn_page(self):
		self.current_page += 1
		print(f"Siz Keyingi sahifaga o'tdingiz. Sahifa: {self.current_page}")

	def restart(self):
		self.current_page = 1
		print(f"Siz 1-sahifaga qaytdingiz! Sahifa: {self.current_page}")


book = Book()
# book.open()
# book.turn_page()
# book.turn_page()
# book.restart()



6.



class Dog:
	total_dogs = 0
	def __init__(self, name="Rex"):
		self.name = name
		Dog.total_dogs += 1

	@classmethod
	def get_total_dogs(cls):
		return cls.total_dogs

# dog = Dog("Rex")
# dog2 = Dog("Simba")
# dog3 = Dog("Sharik")


# print(f"Umumiy itlar soni: {Dog.total_dogs}")



7. 


class Computer:
	total_computers = 0 
	computers_list = []

	def __init__(self, name):
		self.name = name
		self.computers_list.append(name)
		Computer.total_computers += 1

	@classmethod
	def add_computer(cls):
		return f"Kompyuterlar ro'yxati: {cls.computers_list}, Hozirda mavjud bo'lgan Kompyuterlar soni: {cls.total_computers}"


# PC = Computer("Lenovo")
# PC2 = Computer("MSI")
# PC3 = Computer("HP")
# print(PC.add_computer())


8. 


class Employee:
	total_employees = 0
	employees_list = []

	def __init__(self,name):
		self.name = name
		self.employees_list.append(name)
		Employee.total_employees += 1

	@classmethod
	def hire_employee(cls):
		return f"Ishxonadagi xodimlar soni: {cls.total_employees}\nIshxonadagi xodimlar: {cls.employees_list}"


# xodim = Employee("Ali")
# xodim = Employee("Vali")
# xodim = Employee("Aziz")
# xodim = Employee("Mansur")

# print(xodim.hire_employee())


9.

class Television:
	total_sum = 0
	tv_count = 0 
	average_screen_size = 45
	def __init__(self, size):
		self.size = size
		Television.tv_count += 1
		Television.total_sum += size 
		Television.average_screen_size  = Television.total_sum // Television.tv_count

	@classmethod
	def update_average_screen_size(cls):
		return f"Televizor ulchami: {cls.average_screen_size}, Televizorlar soni: {cls.tv_count}"


# tv = Television(50)
# tv = Television(45)
# tv = Television(50)
# tv = Television(62)
# tv = Television(50)

# print(tv.update_average_screen_size())


10.


class Course:
	total_courses = 0
	courses_list = []

	def __init__(self,course):
		self.course = course
		Course.total_courses +=1 
		Course.courses_list.append(course)

	@classmethod
	def add_course(cls):
		return f"Kurslar Soni: {cls.total_courses}\nKurslar: {cls.courses_list}\n"


# kurs = Course("Ingliz tili")
# kurs = Course("Rus tili")
# kurs = Course("Matematika")
# kurs = Course("Adabiyot")

# print(kurs.add_course())



11.

class Math:
	@staticmethod
	def math(a,b):
		return a * b


# mat = Math()
# print(mat.math(5,5))


12.


class Temperature:
	@staticmethod
	def celsius_to_fahrenheit(a):
		c = (a*1.8)+32
		return f"{a} Gradus Selsiy {int(c)} Farengeytga teng."

# a = int(input("Raqam kiriting: "))
# gradus = Temperature()
# print(gradus.celsius_to_fahrenheit(a))


13.


class Distance:
	@staticmethod
	def miles_to_kilometers(a):
		m = a*1.609344
		return f"{a} Mil {round(m,2)} Kilometrga teng!"

# a = int(input("Nechi milni kilometrga o'tkazish lozim: "))
# mas = Distance()
# print(mas.miles_to_kilometers(a))


14.


class Utility:
	@staticmethod
	def is_even(b):
		if b %2 == 0:
			return f"{b} juft son!"
		elif b%2 != 0:
			return f"{b} toq son!"
		else:
			return "Xato mal'umot kiritdingiz!"


# b = int(input("Butun soni kiriting: "))
# util = Utility()
# print(util.is_even(b))


15.


class Time:
	@staticmethod
	def seconds_to_minutes(c):
		minut=c//60
		soniya = c % 60
		
		return f"{c} sekund {(int(minut),int(soniya))} ga teng!"


# c = float(input("Vaqtni soniyada kiriting: "))
# vaqt = Time()
# print(vaqt.seconds_to_minutes(c))




16.

class SmartPhone:
	def __init__(self, name, os_version=14, imei=123456):
		self.name = name
		self._os_version = os_version
		self.__imei = imei

	
	def show_info(self):
		return f"Telefon ma'lumotlari:\nNomi: {self.name}\nOS Versiyasi: {self._os_version}\nImei kodi: {self.__imei}"


# tel = SmartPhone("Iphone 14 Pro",17, 12345)
# print(tel.show_info())