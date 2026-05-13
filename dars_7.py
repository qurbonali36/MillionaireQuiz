
# ================String Methods==============


# 1.String metodlari | string methods 


# capitalize-bosh harfni kattalashtiradi.

xat = "assalomu aleykum, mening dasturimga xush kelibsiz."

u = xat.capitalize()

print(u)

# Result: Assalomu aleykum, mening dasturimga xush kelibsiz.


# 2.casefold-hammasini kichik harfga o'tkazadi.

yozuv = "Men Hozir Uyga Vazifani Bajariypaman."

c = yozuv.casefold()

print(c)

# Result: men hozir uyga vazifani bajariypaman.



# 3.center-yozuvni markazga utkazadi.

gap = "Maktab"

m = gap.center(20)

print(m)

# Result:        Maktab     


# 4.count-gapda so'zlar nechi marta takrorlangani ko'rsatadi.

soz = "Uyga vazifa: Men hozir Uyga vazifa uchun gap yoziyapman."

s = soz.count("Uyga vazifa", 8, 40)

print(s)

# Result: 1


# 5.endswith-oxiridagi gapni tekshirish uchun.

word = "Salom dunyo"

w = word.endswith("world")

print(w)

# Result: False


# 6. startswith-boshlanishini tekshirish uchun.

words = "hello world"

ws = words.startswith("hello")

print(ws)

# Result: True


# 7. expandtabs-probelni bo'shliqga o'zgartiradi.

text = "S\tA\tL\tO\tM"

t = text.expandtabs(4)

print(t)

# Result: S   A   L   O   M


# 8.find-belgilagan satridan kiritilgan qiymatni qidiradi.

text = "Assalomu aleykum,  bu mening dasturim. "

t = text.find("mening")

print(t)

# Result: 22 


# 9. Index-belgilagan satridan kiritilgan qiymatni qidiradi | find-dan farqi "ValueError: substring not found" 

ism = "Mening ismim Qurbonali. Yoshim 16-da"

i = ism.index("Qurbonali")

print(i)

# Result: 13

# 10. isalnum-Satrda ko'radi alphabet va number ishtirok etganmi yoki yo'q / tekshiradi / faqat num va alphabet-ni 

alnumeric = "Qurbonali2010"

al = alnumeric.isalnum()

print(al)

# Result: True

# 11. isalpha-Satrda ko'radi alphabet ishtirok etganmi yoki yo'q / tekshiradi / faqat alphabet-ni

alp = "Ergashev"

a = alp.isalpha()

print(a)

# Result: True

# 12. isascii-Satrda keltirilgan qiymat ascii jadvalida bormi yoki yo'q tekshiradi.

txt = "Python Dasturlash tili 2026"

t = txt.isascii()

print(t)

# # Result: True

# 13. isdecimal-satrda 0-9  bor yo'qligini tekshiradi.

txt = "06"

tx = txt.isdecimal()

print(tx)

# Result: True

# 14. islower-Barchasi kichik harfda yozilganini tekshirradi.

kichik = "dasturlash"

k = kichik.islower()

print(k)

# Result: True

# 15. isprintable-chqarishga mosi yoki yo'q shunga javob beradi.

chiqarish = 'Men dasturlashda №1 Bo\'lmoqchiman'

ch = chiqarish.isprintable()

print(ch)

# Result: True

# 16. join-listdan satrga/stringga o'tkazadi

varoq = ["Ergashev", "Qurbonali", "Usmonalievich"]

v = " | ".join(varoq)

print(v)

# Result: Ergashev | Qurbonali | Usmonalievich

# 17. split-stringdan listga o'tkazadi.

sp = "Men kelajakda eng zo'r dastruchi bo'laman."

s = sp.split()

print(s)

# Result: ['Men', 'kelajakda', 'eng', "zo'r", 'dastruchi', "bo'laman."]

# 18. strip-satrning kesilgan qismini qaytaradi.

satr = "     olma     "

s = satr.strip()

print("Men yoqtiradigan mevalardan biri bu " + s)  

# Result : Men yoqtiradigan mevalardan biri bu olma


# 19. upper-satrni barchasini katta harfga o'tkazadi.

up = "🔎men umrimda buncha xat yozmagandim😅"

u = up.upper()

print(u)

# Result: 🔎MEN UMRIMDA BUNCHA XAT YOZMAGANDIM😅


# 20. zfill/zero fill-satrga nollar qo'shadi.

nol = "2010"

n = nol.zfill(2010)  #Terminalni kattaroq qilib ishga tushiring😄😅.

print(n)


# 21. rfind-satrning  kiritilgan qiymatni topadi.

find = "Men kod yozishga qiziqaman"

f = find.rfind("qiziqaman")

print(f)

Result: 17


# 22. replace-Ingiliz tildan olingan bo'lib almashtirish ma'nosini beradi.

rep = "Men hozir kod yoziyapman. Ertaga Middle darjasiga erishaman."

r = rep.replace("Ertaga", "7-Oyda")

print(r)

# Result: Men hozir kod yoziyapman. 7-Oyda Middle darjasiga erishaman.


# 23. isupper-Barchasi katta harfda ekanligini tekshiradi.

katta = "MEN BARCHA YOZUVLARNI KATTA HARFDA YOZIYAPMAN."

k = katta.isupper()

print(k)

Result: True


# 24. isspace-yozuvda probel borligini tekshiradi.

probel = "      "

p = probel.isspace()

print(p)

# Result: True

# 25. title-Satrni barcha so'zlarni bosh harflarini katta harfga o'zgartiradi.

title = "Men kodni yozib tugatdim👋🏻"

t = title.title()

print(t)

# Result: Men Kodni Yozib Tugatdim👋🏻

# 26. swapcase-Satrdagi katta harflarni kichik, kichik bo'lsa katta harfga o'tkazadi.title

sw = "MeN QuRbOnAlImAn"

s = sw.swapcase()

print(s)

# Result: mEn qUrBoNaLiMaN

# 27.translate-Ingliz tilidan olinib dastrulashga o'girish yane komyuter tiliga uzgartirish degan manoni beradi.(ascii jadvalidan foydalanib)

tarj = {80:  83}
t = "Palom Qurbonali!"
print(t.translate(tarj))

# Result: Salom Qurbonali!

# 28. splitlines-stringni qatorlarga ajratib (linesga) listga o'tkazadi.

spl = "Assalomu aleykum\nhurmatli ustoz"

s = spl.splitlines()

print(f"28. splitlines Natijasi: {s}")

# Result: ['Assalomu aleykum', 'hurmatli ustoz']

# 29. isdigit-Stringda faqat raqam bor yo'qligin tekshiradi.

raqam = "32010"

r = raqam.isdigit()

print(f"29. Isdigit Natijasi: {r}")

# Result: True

# 30. partition-Satrda belgilangan qiymatdan ajratib turib tuple-ga o'giradi.

txt = "Men uyga vazifani 100% bajarib bo'ldim✅."

t = txt.partition("100%")

print(f"30. Partition Resultati: {t}")

# Result: ('Men uyga vazifani ', '100%', " bajarib bo'ldim✅.")


# ==========================Uyga Vazifa Bajarildi✅================================