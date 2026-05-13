1.

class Texnika:
	def __init__(self, brand="Chevrolet", model="Laceti", type="Car"):
		self.brand = brand
		self.model = model
		self.type = type
	def info(self):
		print("="*120, "\n")
		print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type} \n")
		print("="*120)

class Notebooks(Texnika):
	def __init__(self, brand="Lenova", model="82C3", type="Notebook",video_card="RTX 5090", ram = "8 GB", display="1366 x 768 (R)"):
		super().__init__(brand, model, type)
		self.video_card = video_card
		self.ram = ram
		self.display = display


	def  more_info(self):
		print("="*120, "\n")
		print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Video card: {self.video_card}, RAM: {self.ram}, Display: {self.display} \n")
		print("="*120)


class Televisions(Texnika):
	def __init__(self, brand="Artel", model="Smart TV", type="Television", size=45, display="HD"):
		super().__init__(brand, model, type)
		self.size = size
		self.display = display
	def more_info(self):
		print("="*120, "\n")
		print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Size: {self.size}, Display: {self.display} \n")
		print("="*120)


class Smartphones(Texnika):
	def more_info(self, brand="Apple", model="Iphone", type="IOS", size="Unknown", sim_count=1):
		print("="*120, "\n")
		print(f"Brnad: {brand}, Model: {model}, Type: {type}, Size: {size}, Sim count: {sim_count} \n" )
		print("="*120)


# t = Texnika()
# t.info()

# tex = Notebooks()
# tex.more_info()

# texnik = Televisions()
# texnik.more_info()

# texnika = Smartphones()
# texnika.more_info()




2.

class Transport:
	def __init__(self, brand="Tesla", model="Unknown", type="Unknown"):
		self.brand = brand
		self.model = model
		self.type = type

	def info(self):
		print("="*120, "\n")
		print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type} \n")
		print("="*120)

class ElectroCars(Transport):
	def __init__(self, brand="Tesla", model="Unknown", type="Unknown", battery_life="Infinite year", chargin_time="12 hours"):
		super().__init__(brand, model, type)
		self.battery_life = battery_life
		self.chargin_time = chargin_time

	def more_info(self):
		print("="*120, "\n")
		print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Battery life: {self.battery_life}, Chargin time: {self.chargin_time} \n")
		print("="*120)

class SportCars(Transport):
	def __init__(self, brand="Lamborghini", model="Venono", type="Sport Car / Hyper Car", motor="V8", color="Black"):
		super().__init__(brand,model,type)
		self.motor = motor
		self.color = color

	def more_info(self):
		print("="*120, "\n")
		print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Motor: {self.motor}, Color: {self.color} \n")
		print("="*120)


class Truck(Transport):
	def __init__(self, brand="Super Truck", model="Unknown", type="Truck", height="No Information", long="Unknown", wieght="No Information"):
		super().__init__(brand, model, type)
		self.height = height
		self.long = long
		self.wieght = wieght

	def more_info(self): 
		print("="*120, "\n")
		print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Height: {self.height}, Long: {self.long}, Weight: {self.wieght} \n")
		print("="*120)




# tr = Transport()
# tr.info()

# tran = ElectroCars()
# tran.more_info()

# transport = SportCars()
# transport.more_info()

# tr2 = Truck()
# tr2.more_info()







3.

class University:
	def __init__(self, university="Garvard"):
		self.university = university

	def info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university}\n")
		print("="*120, "\n")

class Staff(University):
	def __init__(self, university="Garvard", first_name="Qurbonali", last_name="Ergashev", age=20):
		super().__init__(university)
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def staff_info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university},  First name: {self.first_name},  Last name: {self.last_name},   Age: {self.age}\n")
		print("="*120, "\n")

class Student(Staff):
	def __init__(self, university="Garvard", first_name="Qurbonali", last_name="Ergashev", age=20, group="IT / Programers"):
		super().__init__(university,first_name,last_name,age)
		self.group = group

	def more_info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university},  First name: {self.first_name},  Last name: {self.last_name},   Age: {self.age},   Group: {self.group}\n")
		print("="*120, "\n")


class Teacher(Staff):
	def __init__(self, university="Garvard", first_name="Qurbonali", last_name="Ergashev", position="Teacher", subject="Maths"):
		super().__init__(university,first_name,last_name)
		self.position = position
		self.subject = subject

	def more_info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university},  First name: {self.first_name},  Last name: {self.last_name},  Position: {self.position},  Subject: {self.subject}\n")
		print("="*120, "\n")

class OtherStaff(Staff):
	def __init__(self,university="Garvard", first_name="Qurbonali", last_name="Ergashev", position="Staff"):
		super().__init__(university,first_name,last_name)
		self.position = position

	def more_info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university},  First name: {self.first_name},  Last name: {self.last_name},   Position: {self.position}\n")
		print("="*120, "\n")


# univer = University()
# univer.info()

# staf = Staff()
# staf.staff_info()

# stud = Student()
# stud.more_info()

# teach = Teacher()
# teach.more_info()

# othstaf = OtherStaff()
# othstaf.more_info()







4.


class Object(University):
	def __init__(self, university="Garvard", name="Computer and Mebel"):
		super().__init__(university)
		self.name = name

	def object_info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university},   Name: {self.name}\n")
		print("="*120, "\n")

class Computer(Object):
	def __init__(self,university="Garvard", name="Computer", soni="24", tizimi="Ma'lumot topilmadi!", holati="Yangi"):
		super().__init__(university,name)
		self.soni = soni
		self.tizimi = tizimi
		self.holati = holati

	def object_more_info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university},   Name: {self.name},   Soni: {self.soni},  Tizimi: {self.tizimi},   Holati: {self.holati}\n")
		print("="*120, "\n")

class Mebel(Object):
	def __init__(self, university="Garvard", name="Mebel", soni=40, turi="Ma'lumot topilmadi!", holati="O'rtacha"):
		super().__init__(university,name)
		self.soni = soni
		self.turi = turi
		self.holati = holati

	def object_more_info(self):
		print("="*120, "\n")
		print(f"Universitiy: {self.university},   Name: {self.name},   Soni: {self.soni},  Turi: {self.turi},   Holati: {self.holati}\n")
		print("="*120, "\n")


# ob = Object()
# ob.object_info()

# com = Computer()
# com.object_more_info()


# meb = Mebel()
# meb.object_more_info()