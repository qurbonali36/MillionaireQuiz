funksion = """

#      ____        _   _                      
#     |  _ \ _   _| |_| |__   ___  _ __       
#     | |_) | | | | __| '_ \ / _ \| '_ \      
#     |  __/| |_| | |_| | | | (_) | | | |     
#     |_|    \__, |\__|_| |_|\___/|_| |_|     
#            |___/                            
#   ---------------------------------------
#                 "FUNKSIYA"



"""
print(funksion)




# 1. funkisyalar.

def user_data(first_name, last_name, age):
	information = f"""

||Ism: {name}			|
||Familiya: {surname}   	|
||Yosh: {age}			|
	
"""
	return information
	

name = input("ismingiz: ")
surname = input("Familiyangiz: ")
age = input("Yoshingiz: ")
print("=_="*20)

print(user_data(name, surname, age))


def user_data2(first_name, last_name, age):
	return first_name, last_name, age
 
name = input("ismingiz: ")
surname = input("Familiyangiz: ")
age = input("Yoshingiz: ")
# info = f"""
# Ism: {name}
# Familiya: {surname}
# Yosh: {age}
# """
print(*user_data2(f"Ism: {name}", f"Familiya: {surname}", f"Yosh: {age}"), sep='\n')




# 2.Funksiyalar


def find_max(a,b,c):
    result = max(a,b,c)
    max_names = []
    if a == result:
        max_names.append("A")

    if result == b1:
        max_names.append("B")

    if result == c1:
        max_names.append("C")
    yakuniy_javob = " va ".join(max_names)
    print(f"Eng katta son {yakuniy_javob} = {result}")

a1 = float(input("a = "))
b1 = float(input("b = "))
c1 = float(input("c = "))

find_max(a1, b1,c1)


# 3.Funksiyalar

def find_letter_count(word, letter):
    son = word.count(letter)
    print(f"'{word}' so'zida '{letter}' dan {son} ta")

Word = input("So'zni/gapni yozing: ")
Letter = input("Qaysi harfni/so'zni qidirmoqchisiz? ")
find_letter_count(Word, Letter)



# 4.Funksiyalar

def list_sum(my_list):
    print(f"Listning elementlar yig'indisi = {sum(my_list)}")

MY_list = [1,2,3,4,5,9]
list_sum(MY_list)

# 5.Funksiyalar

def daraja(a,b):
    return int(a) ** int(b)
A = int(input("A = "))
B = int(input("B (daraja) = "))

print(daraja(A,B))

# 6. Funksiyalar

def daraja4(a,b,c,d):
	kup = a**b
	kup2 = a**c
	kup3 = a**d
	kup4 = kup*kup2*kup3
	results = f""" 
	1. {a}-ning {b}-chi darajasi = {kup}
	2. {a}-ning {c}-chi darajasi = {kup2}
	3. {a}-ning {d}-chi darajasi = {kup3}
	4. {a}-ning {b,c,d}-chi darajalarini kupaytmasini natijasi = {kup4}

	"""
	return results
A = int(input(" A = "))
B = int(input(" B (Daraja) = "))
C = int(input(" C (Daraja) = "))
D = int(input(" D (Daraja) = "))
print(daraja4(A,B,C,D))


# 7.Funksiyalar


def digit_count_and_sum(word):
	sanoq = 0
	yigindi = 0
	for i in word:
		if i.isdigit():
			i = int(i)
			sanoq += 1
			yigindi += i
	print(f"Raqamlar yig'indisi = {yigindi}, Raqamlar soni = {sanoq}")
	 


word1 = input("Birorta so'z yozing: ")
digit_count_and_sum(word1)

# 8. Funksiyalar

def add_right(a, b):
	natija2 = a + b
	print(f" a ni o'ng tarafiga b ni  qo'shsak =  {natija2} - hosil bo'ladi.")


Q = input(" a = ")
W = input(" b = ")
add_right(Q , W)

# 9.Funksiyalar

def add_left(a, b):
	natija2 = b+a
	print(f" a ni chap tarafiga b ni  qo'shsak =  {natija2} - hosil bo'ladi.")


A = input(" a = ")
B = input(" b = ")
add_left(A , B)



# 10.Funksiyalar
a = [32, 3, 25, 5, 16, 4]
def work_with_list(a):
	kichik = min(a)
	for i in range(len(a)):
		a[i] = kichik * a[i]
		
		
	print(a)

work_with_list(a)


# 11.Funksiyalar

def big_sales(sales):
	max_summa = 0
	max_oy = " "
	min_summa = 12000
	min_oy = " "
	for month, sale  in sales.items():

		if sale > max_summa:
			max_summa = sale
			max_oy = month

		if sale < min_summa:
			min_summa = sale
			min_oy = month
	natija2 = f"""
	=========================================
	Eng ko'p daromad keltirgan oy = {max_oy}
	
	Daromad summasi = {max_summa}
	=========================================
	-----------------------------------------
	=========================================
	Eng kam oy = {min_oy}
	
	Daromad summasi = {min_summa}
	=========================================

	"""
	return natija2



SaleS = {
  "yanvar": 12000,
  "mart": 6000,
  "aprel": 15000,
  "sentabr": 9000,
  "dekabr": 10000,
  "may": 25000,
  "iyun": 2000,

}


print(big_sales(SaleS))


# 12.Funksiyalar

def min_max(numbers, max_num, min_num):
	katta_son = max(numbers) 
	kichik_son = min(numbers)
	if max_num == katta_son :
		result_number = f"Barakala siz eng katta sonni topdingiz! Eng katta son = {katta_son}"
	else:
		result_number = f"Afsus, Siz biroz xatolikga yo'l qo'ydingiz! To'g'ri javob : {katta_son}"
		
	if min_num == kichik_son:
		result_numbers = f"Barakala siz eng kichik sonni topdingiz! Eng katta son = {kichik_son}"
		
	else:
		result_numbers = f"Afsus, Siz biroz xatolikga yo'l qo'ydingiz! To'g'ri javob : {kichik_son}"
	return f"\n--- NATIJA ---\n1) {result_number}\n2) {result_numbers}"


numbers = [20, 30, 5, 45, -12, -8]
print(f"Bizda bor raqamlar: {numbers}")
max_number = int(input("Eng katta son qaysi? "))
min_number = int(input("Eng kichik son qaysi? "))
print(min_max(numbers, max_number, min_number))



# 13.Funksiyalar



def expensiveProduct(products):
	Qiymat_telefon_narx = 0
	Qiymat_telefon_nomi = " "
	for product in products:
		if product["price"] > Qiymat_telefon_narx:
			Qiymat_telefon_narx = product["price"]
			Qiymat_telefon_nomi = product["name"]

	return f"Eng qiymat telefon: {Qiymat_telefon_nomi} bo'ladi. Uning narxi {Qiymat_telefon_narx}"




products = [
  {
    "name": "Iphone X",
    "price": 600
  },
  {
    "name": "Iphone 12",
    "price": 1500
  },
  {
    "name": "Samsung Note 9",
    "price": 800
  },
  {
    "name": "Samsung S10",
    "price": 1100
  },
  {
    "name": "Samsung S25 ultra",
    "price": 1800
  },
]
print("_"*20)
print(expensiveProduct(products))