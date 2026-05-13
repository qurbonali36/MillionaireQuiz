# Kiritilgan qiymatni o'qib olamiz
x = int(input("son: "))

# O'tgan to'liq kunlarni hisoblaymiz
kunlar = (x - 1) * 365
print(kunlar)
# Yil va kunni topamiz
yil = (kunlar // 364) + 1
print(kunlar // 364)

kun = (kunlar % 364) + 1
print(kunlar % 364)

# Natijani bitta qatorda, probel bilan chiqaramiz
print(f"{yil} {kun}")




# import sys

# def solve():
#     # Oddiy input() o'rniga juda tez ishlaydigan o'qish funksiyasini yozamiz
#     def get_ints():
#         return map(int, sys.stdin.readline().split())
        
#     # 1. N sonini o'qib olamiz
#     n_qator = sys.stdin.readline()
#     if not n_qator:
#         return
#     N = int(n_qator)

#     # Agar umuman modul bo'lmasa, javob 0
#     if N == 0:
#         print(0)
#         return

#     # 2. Boshlang'ich holatni o'rnatamiz
#     max_uzunlik = 1
#     hozirgi_uzunlik = 1

#     # Eng birinchi toshni o'qiymiz (unga faqat oldingi o'ng port kerak)
#     _ , oldingi_ong = get_ints()

#     # 3. Qolgan toshlarni tsiklda birma-bir o'qib tekshiramiz
#     for _ in range(1, N):
#         hozirgi_chap, hozirgi_ong = get_ints()
        
#         # DOMINO QOIDASI: Oldingi o'ng tomon hozirgi chap tomonga tengmi?
#         if oldingi_ong == hozirgi_chap:
#             hozirgi_uzunlik += 1  # Zanjir uzaydi!
#         else:
#             hozirgi_uzunlik = 1   # Zanjir uzildi! Shu toshdan yangi zanjir boshladik.
            
#         # Agar hozirgi zanjirimiz biz bilgan maksimaldan ham o'tib ketsa, yangilaymiz
#         if hozirgi_uzunlik > max_uzunlik:
#             max_uzunlik = hozirgi_uzunlik
            
#         # Keyingi aylanma uchun hozirgi tosh endi "oldingi" toshga aylanadi
#         oldingi_ong = hozirgi_ong

#     # 4. Yakuniy eng katta natijani chiqaramiz
#     print(max_uzunlik)

# # Dasturni ishga tushirish
# if __name__ == '__main__':
#     solve()




class Person:
   origin_country = "USA"

   def __init__(self, name="Unknown", age="?", gender="Unknown"):
     self.name = name
     self.age = age
     self.gender = gender

   def speak(self, words):
     print(f"{self.name} speaks: {words}")


class Employee(Person):
   def __init__(self, name="Unknown", age="?", gender="Unknown", salary=1500, job_title="IT"):
     super().__init__(name, age, gender)
     self.salary = salary
     self.job_title = job_title

   def display_info(self):
     print(f"Employee {self.name} works as a {self.job_title}")




# per = Employee()
# per.display_info()





