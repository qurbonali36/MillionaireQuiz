# Importlar:

from avto_rang import aprint   #o'zi avtomatik yozuvlarga rang beradi. Ozimni faylim bo'lgani uchun ishlatmadim.
from copy import  deepcopy   #copy kutubxonasidan deepcopyni chaqiramiz.
from collections import Counter  #Collections kutubxonasidan Counter(Hisoblagichni) chaqiriyapmiz.


# 0. Dict yasash ussulari

# lugat = {"Maktab": 12, "Talabalar": "600-ta talaba "}
# lug = dict(Maktab = 12, Talabalar = "600-ta talaba ")
# l = dict([("Maktab",12), ("Talabalar", "600-ta talaba ")])

# print("_"*45)
# print(lugat)
# print("_"*45)
# print(lug)
# print("_"*45)
# print(l)
# print("_"*45)


# 0.3 Copy bilan ishlash
# son = [5,6,7,8]
# s = son.copy()
# s.append(9)
# print(son)

# 0.6 Deepcopy bilan ishlash
# q = [1,4,3,2,[5,6,7]]
# u = q.copy()
# u.append(8)
# print(q)
# print(u)

# 0.Deepcopy ni ishlatamiz.
# Q = [1,4,3,2,[5,6,7]]
# U = deepcopy(Q)
# U[4].append(8)
# print(Q)


# 0.9 Counter ni ishlatamiz

# raqam = [1,2,3,4,5,6,5,6,6,6,6,]
# hisob = Counter(raqam)
# print(hisob)


# 1. Clear methodi
# dars = {
#     "Fan:": "Informatika",
#     "Vaqti:": "2-saot",
#     "ustoz:": "Shamsidinov Sh"
# }
# print("-------------- Avval ---------------")
# print(dars)
# dars.clear()
# print("-------------- Keyin ---------------")
# print(dars, "-- Clear metodi ishlatildi.")

# 2. Copy  methodi

# super_car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964

# }

# ford = super_car.copy()
# print(ford)

# 3. Fromkeys methodi

# malumot = (" A qiymat teng ", "B qiymat teng ")
# mal = 20

# umumiy = dict.fromkeys(malumot, mal)
# print(umumiy)


# 4.Get methodi

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.get("brand")

# print(x)


# 5. Items methodi

# malumot = {"Ism": "Qurbonali", "Familiya": "Ergashev", "Yosh": 16}
# m = malumot.items()

# print(m)

# 6. Keys  methodi

# maktab = {
#     "Fan": "matematika",
#     "Vaqti": "2-soat",
#     "Ustozi": "Qulfidinov F"
# }

# mak = maktab.keys()
# print(mak)



# 7.Pop methodi

# sinf_info = {
#     "8a": "33-ta talaba",
#     "8b": "30-ta  talaba",
#     "9a": "28-ta talaba"
# }

# s = sinf_info.pop("8a")

# print("_______________________Pop dan keyin➡________________________")
# print(sinf_info)
# print("____________Popni olgan qiymatni tenglaganimizda➡____________")
# print(s)


# 8. Popitem methodi

# kitob = {
#     "Kitob nomi:": "Yoddoshtho",
#     "Kim yozgan:": "Sadriddin Ayni",
#     "Yili": None
# }

# k = kitob.popitem()

# print(kitob)
# print("--"*31)
# print(k)

# 9. Setdefault methodi

# log_par = {
#     "Login": "ErgashevQ",
#     "Parol": "e1g1s1o1w"

# }

# l = log_par.setdefault("user", "Ergashev_Qurbonali")

# print("_"*74)
# print(l)
# print("_"*74)
# print(log_par)
# print("_"*74)


# 10. Update methodi

# phones = {
#     "Name": "Samsung S26 Ultra",
#     "Year": 2026
# }

# phones.update({"New character": "Stabilization"})

# print("-"*80)
# print(phones)
# print("-"*80)

# 11. Values methodi

# laptop = {
#     "Name": "Macbook",
#     "Brend": "Apple",
#     "Model": "M4",
#     "Cost": "Unknown"
# }

# lap = laptop.values()
# top = laptop.keys()
# print("_____________________-Dictionary-____________________")
# print(laptop)
# print("_______________________--Keys--______________________")
# print(top)
# print("_______________________-Values-______________________")
# print(lap)
