# ================List Methods==================
 
# 1. append - Bu listning oxirida faqat bitta object qo'shadi.

app = ["Python", "Java", "JavaScript", "C#", "C++"]

print("________________👋🏻Assalomu aleykum_______________")
print("Bugun biz sizlar bilan ==========List Methods========== haqida gaplashamiz📄.")
print("Birinchi List Method bu bizda append. Hozir Biz bu kod haqida gaplashamiz.")
input("Boshladikmi? (Davom etish uchun Enter bosing) ")
print(f"Bizda hozir shu lsit {app} mavjud")
print("Sen  bu listga yetishmayotgan bitta eng mashhur dasturlash tillaridan birini qo'shasiz.")
program = input("Qaysi dasturlash tilini qo'shmoqchisiz? ")

# o'rganish osonroq bo'lishi uchun uni yana answerga o'tkazdim.
answer = program

# Gemini orqali while ishlashini shunib oldim va uni bu yerda ishlatdim.
while answer in app:
	print("Bu dasturlash tili mavjud! Boshqa dasturlash tilini kiriting.")
	answer = input("Qaysi dasturlash tilini qo'shmoqchisiz?")

# Dastur davom etadi...
app.append(answer)
print(f"Xo'p yaxshi sen hozir listga shuni {answer} qo'shding.")
print(f"Hozir sening Listingning to'liq ko'rinishi: {app} shu ko'rinishda.")
print("Barakala, siz append ishlatishni menga o'rgatdingiz😅")
input("Davom etamizmi (Davom etish uchun Enter bosing) ? ")

keying10 = """

       Keyingi method →

"""
print(keying10)


# 2.Extend - bu listga bir nechta qiymat qo'sha oladi.(oxirida)

cars = ["BMW", "Lamborghini", "Merc", "Nexia 2"]
print("Qani unda biz keyingi dasrga ya'ne extend mavzusiga o'tamiz...")
input("extend mavzusini boshlash uchun Enter bosing...")
print("Extend bu listning oxiriga bir nechta qiymat qo'sha oladi. append esa bitta. Bu narsa yoddan chiqmasin!")
extend = input("Shunarlimi? (Enter bosing) ")

print("Ana endi extendni sinab ko'ramiz")
print(f"Sizda {cars} shu list bor. Endi siz o'ziz yoqtradigan mashinalarni ro'yxatini kiritishingiz lozim.")
user = input("Qaysi mashinalarni qushmoqchisiz?  ")
input(f"Siz hozir listga shularni {user} qo'shmoqchsiz? ishonchingiz komilmi?(Enter==Ha)") 
cars.extend(user)
print(f"Natija: {cars} --- G'alati chiqdimi😅 Bu bir extendni kamchiligi desak bo'ladi nimagaki u har bitta harf va xatto probelni listga alohifda qilib kuchiradi.")

keying09 = """

       Keyingi method →

"""
print(keying09)


# 3. count - listdagi kiritilgan qiymatlar nechi marta ishlatilganini hisoblaydi.count

print("Endi biz count haqida gaplashamiz. count bu listda kiritilgan qiymatlarda siz kiritgan qiymat nechi marotaba takrorlanganini chiqaradi.")
print("Qani bir sinab ko'raylikchi...")
matn = """
Python juda kuchli dasturlash tili. Python tili yordamida sun'iy intellekt, 
veb-saytlar va ma'lumotlar tahlili bilan shug'ullanish mumkin. Python o'rganish juda qiziqarli!
"""
takror = int(input(f"{matn} --- Shular orasidan python so'zi nechi marotaba takrorlangan?"))
answer = matn.count("python")
if takror == answer:
    print(f"🎊Barakala sen tupa-tug'ri topding🎉. Javob: {answer}") 

while takror != answer:
	print("Bu javob xato qaytadan hisoblang.")
	takror = int(input("Yana urinib ko'ring: "))
	
print(f"🎊Barakala sen tupa-tug'ri topding🎉. Javob: {answer}")

keying08 = """

       Keyingi method →

"""
print(keying08)

# 4. index -  bu listda biz kiritgan qiymat nechinchi raqam yane indexda😄 turayotganini aytadi.

print("Endi esa biz index haqida gaplashamiz.")
index1 = """

Index bu listga kiritgan qiymatimizni indeksi ya'ne nechinchi raqamda 
yoki xonada turganini bilish uchun kerak bo'ladi.

"""
print(index1)

shunmoq = input("Shungdingmi?(Ha/Yo'q) ")
# if shunmoq == ["HA","Ha","ha",""]:
# 	print("ajoyib👍")
while shunmoq not in ["HA","Ha","ha","h"]:
	print(index1)
	shunmoq = input("Endichi Shungdingizmi? ")

print("ajoyib👍")

print("Unda indexga bitta misol ko'ramiz: ")
indeks_misol = ["Uyg'onish", "Yuz qulni yuvish", "Nonushta qilish", "Maktab"]
indeks_javob = int(input(f"Mana shu misolda: {indeks_misol} -- Yuz nechinchi indeksda? "))

while indeks_javob != 1:
	print("Notug'rii😔.")
	savol = input("Qaytadan urinib ko'ring. Sonni ayting: ")

print("🎉Barakala Sen juda ham tug'ri jvob berding.🎉")

keying07 = """

       Keyingi method →

"""
print(keying07)

# 5.insert - bu listning istagan positsiyasida yane istagan joyiga qiymat qo'sha oladi.

print("Biz insert mavzusiga ham yettib keldik😎.")
ins = """ 

insert - bu listning istagan positsiyasida yane istagan
joyiga qiymat qo'sha oladi.(indeksini kiritish orqali)

"""
print("Qani unda darsni boshladik: ")
savol_insert = ["Assalomu", "Yaxshimisiz?"]
savol_2 = input(f"Sizda shu {savol_insert} - list mavjud. Sen listga mantiqan to'liq bo'lishi uchun qayerga qaysi jumlani qo'yishni aytasan! (enter bosing)")
toldirish = input("So'z : ")
toldirish_2 = int(input("index(faqat raqam): "))

while toldirish_2 != 1 or toldirish != "aleykum":
	print("Xatttooo🙁")
	print("Qaytadan urinib ko'ring: ")
	toldirish = input("So'z : ")
	toldirish_2 = int(input("index(faqat raqam): "))


print("Tupa tog'ri✅")

savol_insert.insert(toldirish_2, toldirish)
print(f"Sening javobing: {savol_insert}")

keying = """

       Keyingi method →

"""
print(keying)


# 6. pop - Methodi bu metod kiritgan indexsiz bo'yicha listadan ushani olib turadi lekin uchirib tashlamaydi.Balkini uni o'zida saqlab turadi.

pop1 = """

                            ======List Methods======
Pop methodi bu metod kiritgan index-siz (indeks kiritilmasa oxiridagi bittasini olob tashlaydi) bo'yicha listadan ushani olib turadi 
                                                        lekin
uchirib tashlamaydi.Balki uni o'zida saqlab turadi.Keyin siz uni boshqa bir objectga tenglab qo'ysangiz bo'ladi.

"""
print("Biz davom etamiz...")
print("Hozirgi mavzumiz Pop mavzusi.")
write = input("Pop nimaligini bilmoqchi bo'lasingiz, 'Pop' deb yozing! ")
while write not in  ["Pop", "pop", "p", "POP"]:
	print("Pop deb yozing bo'lmasa dastur ishlamaydi!😏")
	write = input("Pop nimaligini bilmoqchimisiz? ")

print(f"{pop1}")

sorash01 = input("Pop nimaligini shundingizmi? ")
if sorash01 in ["ha", "HA", "h","H"]:
	print("Ajoyib👌🏻. Unda Pop ga misol ko'ramiz.")
else :
	print(f"Bu tarifni yana qaytadan yaxshilab o'qib chiqing: {pop1}")

Qurbonali = ["Ergashev", "Qurbonali", "Usmonalievich"]
print("Pop ga misol: ")
print(f"bizda shu list mavjud {Qurbonali} Biz bu listdan istagan bitta qiymatimizni ola olamiz")
olish = int(input("Siz qaysi objektni olmoqchisiz? (~faqat raqam!~) "))
Qurbonali.pop(olish)
print(f" Natija : {Qurbonali}")
print("Endi biz aytganimizdek olgan qiymatimizni nimagadir tenglab qo'yamiz!")
tenglash02 = input("Nimaga tenglashga xoxlaysiz? ")
tenglash02 = Qurbonali.pop(olish)
print(f"Qiymat teng bo'ldi:[{tenglash02}]")

print("Tabriklaymiz🎉. Siz pop mazusini tugatdingiz.")

keying02 = """

       Keyingi method →

"""
print(keying02)

# 7.remove - Bu listdan bitta element ni olib tashlaydi.Buni popdan farqi bu olgan objektni biror narsga umuman teglab bo'lmaydi, ya'ne uchirib tashlaydi.

remov = """

                      =====================List Methods=====================

                                         --->/Remove/<---
Bu siz kiritgan qiymatni faqat bitta qiymatni olib tashlaydi.
Buni pop-dan farqi bu olgan objektni biror narsga umuman teglab bo'lmaydi, ya'ne uchirib tashlaydi.

"""


print("Keyingi darsga ham o'tdik✅")
print("Biz hozir Remove haqida gaplashamaiz. Remove bu: ")
print(remov)
shunish = input("Remove- ni shundngizmi->? ")

if shunish in ["Ha", "ha", "h", "H", "HA"]:
	print("Juda yaxshi😇. Unda missolga o'tamiz: ")
else:
	print(f"Yaxshiroq shunish uchun bu matni yanada diqatliroq o'qib chiqing!:  {remov}")

olmoq = ["O'qish", "Maktab", "Python", "Student", "kitob", "Universitet"]
olmoq1 = ["O'qish", "Maktab", "Python", "Student", "kitob", "Universitet"]
print(f"{olmoq} -- Shu ro'yxatda bitta so'z boshqalaridan farq qiladi? Shuni toping. ")
tasdiq = input("Qaysi biri farq qiladi? ")
olmoq.remove(tasdiq)
print(f"Natija: {olmoq} ")
confirm = input(f"Shu {olmoq} javobni tadiqlaysizmi? ")

while confirm not in ["ha", "HA", "Ha", "h", "H"]:
	print("Bekor qilindi❌")
	olmoqq = input(f"{olmoq1}--Qaysi biri farq qiladi? ")
	confirm = input(f"Shu {olmoq1} javobni tadiqlaysizmi? ")
	olmoq1.remove(olmoqq)

print(f"Ajoyib👍.  Siz bergan javob: {tasdiq}. To'g'ri javob✅ : Python")

keying03 = """

       Keyingi method →

"""
print(keying03)

# 8.reverse - bu bizning listning tarbini o'zgartiradi.

revers = """
     =====================List Methods=====================

                       --->/Reverse/<---
                               &
Revers - bu listning/ro'yxatning tartibini o'zgartiruvchi metod.
                               &


"""
print("Reverse darsiga ham yetib keldik✅")
print(f"Reverse bu:  {revers}")
got = input("Reverse-ni shundingizmi--> ? ")
while got not in ["Ha", "ha", "HA", "h", "H", "albatta"]:
	print(f"Sizga buni qayta o'qishni maslihat beraman.  Reverse:  {revers}")
	got = input("Endi shundingizmi--> ? ")

print("Juda yaxshi💪🏻. Unda missol bilan ishlashni boshlaymiz! ")

mevalar = ["Olma", "Shaftoli", "O'rik", "Qulupnay"]
print(f"Bizga --{mevalar}-- listi berildi✅ ")
print("Endi biz bu listga reverse-ni qullymiz.")
activate = input("Reversni qulash uchun: 'Reverse/activate'-deb yozing!❗ ")
mevalar.reverse()
while activate != "Reverse/activate":
	print("To'g'ri yozing⚠️")
	activate = input("Reverse aktivlashtiring...  ")
	


print(f"Reverse muvaffaqiyatli aktivlashtirildi⚠️:  {mevalar}")

keying04 = """

       Keyingi method →

"""
print(keying04)


# 9. Sort - Bu listdagi qiymatlarni Harflar/Alphabet yoki Raqam/Number bilan tartiblaydi(ketma-ketlikda).

sort = """

                  =====================List Methods=====================

                                      --->/Sort/<---

Bu listdagi qiymatlarni Harflar/Alphabet yoki Raqam/Number bilan tartiblaydi(ketma-ketlikda).
                                        &Lekin&
Ro'yxatda ham alphabet va ham number ishtirok etgan bo'lsa uni tartiblay olmaydi.

"""
print("Biz endi Sort mavzusiga keldik✅")
print(f"Sort bu:  {sort}")
understand = input("Sort mavzusini shundingizmi? ")
while understand not in ["Ha", "ha", "h", "H", "HA"]:
	print(f"Sizga yana bir marta bu matni o'qishingizni maslihat beraman: {sort} -- -- yoki batafsilroq ma'lumot olish uchun : https://www.w3schools.com/python/python_ref_list.asp saytiga tashrif buyuring.")
	understand = input("Sort mavzusini endi shundingizmi? ")

print("A'lo Darajada👍, Endi missollar bilan ishlaymiz.")
ismlar = ["Qurbonali", "Tolibjon", "Ma'murjon", "Muzaffarjon", "Bekzod"]
raqamlar1 = [9,5,3,7,22,100,48,755,1]
print(f"Bizda {ismlar}  va  {raqamlar1} listlari bor.")
print("Siz uni aynan sort orqali sortlasak bo'ladimi yoki yo'q va qaysi turdagi ma'lumotlarga kirishini aytishingiz lozim!")
sortlash = input(f"{ismlar}  sortlasak bo'ladimi? ")
while sortlash not in ["Ha", "ha", "h", "H", "HA", "Albatta"]:
	print("Xato⚠️. Qaytadan urinib ko'ring🔁.")
	sortlash = input(f"{ismlar}  sortlasak bo'ladimi? ")


sortlash1 = input(f"{raqamlar1} sortlasak bo'ladimi? ")
while sortlash1 not in ["Ha", "ha", "h", "H", "HA", "Albatta"]:
	print("Xato⚠️. Qaytadan urinib ko'ring🔁.")
	sortlash1 = input(f"{raqamlar1}  sortlasak bo'ladimi? ")

tips = f"""
{ismlar} -- Qaysi ma'lumot turiga yoki methodga kiradi?
A) String-methodi.
B) Integer-methodi.
C) A va B javoblari to'g'ri.
"""
tip = input(tips)
while tip not in ["a", "A", "A) String-methodi", "a) String-methodi"]:
	print("Xato⚠️. Qaytadan urinib ko'ring🔁")
	tip = input(tips)

turlar = f"""
{raqamlar1} -- Qaysi ma'lumot turiga yoki methodga kiradi?
A) String-methodi.
B) Integer-methodi.
C) A va B javoblari to'g'ri.
D) To'g'ri javob yo'q.
"""
tur = input(turlar)
while tur not in ["b", "B", "B) Integer-methodi", "b) Integer-methodi"]:
	print("Xato⚠️.Qaytadan urinib ko'ring🔁")
	tur = input(turlar)



ismlar.sort()
raqamlar1.sort()
print("Barakala🎉. Siz savollarga tupa-tug'ri javob berdiz✅ ")
print(f"Sortlangan ko'rinishlari: {ismlar}   |   {raqamlar1}")

keying05 = """

       Keyingi method →

"""
print(keying05)

# 10.copy - Listadan nusxa oladi. va biz uni boshqa qiymatga o'tkazsak bo'ladi.sort

Copy = """

    =====================List Methods=====================

                        --->/Copy/<---
📍Copy bu listimizni  butunlay copylaydi/nusxalaydi🛢.
Nusxalangan listni biz biror narsaga tenglaymiz📌. 
Shu holatda oldingi listimiz bunga kuchiriladi/nusaxalanadi🛡.

"""

clear = """

       =====================List Methods=====================

                          ---->/Clear/<----
Clear bu biz ning listda bor bo'lgan barcha narsani uchirib tashlaydi❌.
                                 &LEKIN 
Clear bu Pop-ga o'xshamaydi‼.Chunki bu butunlay listni tozalaydi♻.

"""
print("Vanihoyat oxirgi darsga ham yetib keldik✅")
print("Hozir biz eng sodda mavzulardan biri copy va clear haqida gaplashamiz😎")
print(f"Copy bu: ⬇  {Copy}")
oxirgi = input("Copy-ni shundingizmi⁉  ")
while oxirgi not in ["Ha", "ha", "h", "H", "HA", "Albatta"]:
	print("Shunmagan bo'lsangiz❌. Darsni qaytadan ko'rishingiz mumkin🔂")
	print(f"Copy qaytadan bemalol ko'ravering（＾∀＾●）ﾉｼ :  {copy}")
	oxirgi = input("Copy-ni endi shundingizmi⁉  ")

print("Barakala🎉. Endi biz copyga missollar ko'ramiz🆓 : ")
davlatlar =  ["Uzbekiston", "Amerika", "Rossiya" , "Xitoy"]
print(f"Bizda hozir {davlatlar} list bor✔")
print("Endi biz bu 'davlatlar' listni 'Davlatlar' degan qiymatga tebglashimiz lozim‼ ")
code = input(f"Menga endi qanday qilib bu qiymatni 'Davlatlar-ga nusxalasak bo'ladi? (Kod shaklida yozing‼) ")
while code != "Davlatlar = davlatlar.copy()":
	print(f"Xato⚠️. Bu  {code}   - javob notug'ri❌")
	print("Qaytadan urinib ko'ring🔁")
	code = input(f"Menga endi qanday qilib bu qiymatni 'Davlatlar-ga  nusxalasak bo'ladi? (Kod shaklida yozing‼) ")

Davlatlar = davlatlar.copy()
print(f"Natija: Davlatlar = {Davlatlar} ✅")
print("Barakala🎉.Sizni yangi tajribangiz bilan tabriklyaman🥳")

print(f"Bizda keyingi mavuz bu clear mavzusi: ⬇  {clear}")
understand2 = input("*️⃣Mavzuni shundingizmi⁉")
while understand2 not in ["Ha", "ha", "h", "H", "HA", "Albatta"]:
	print("Shunmagan bo'lsangiz❌. Darsni qaytadan ko'rishingiz mumkin🔂")
	print(f"Marhamat yana bir marta matni o'qib chiqishingiz mumkin🔂  {clear} ")
	understand2 = input("*️⃣Mavzuni endi shundingizmi⁉")

print("Shungan bo'lasngiz ajoyib👍. Endi biz clearga missollar ko'ramiz🆓")
uchirish = ["bu", "bizda" ,"oxirgi","dars","!"]
print(f"Bizda hozir {uchirish}-degan list bor endi  biz bu listni tozalashimiz kerak!")
claer_misol = input("Menga bu 'uchirish' - ni qanday qilib tozalashimizni yozing‼⌨️(Kod shaklida)" )
while claer_misol != "uchirish.clear()": 
	print("Xato⚠️. Qaytadan urinib ko'ring🔁")
	misol02 = ("&")
	misol02.center(30)
	print(misol02)
	claer_misol = input("Menga bu 'uchirish' - ni qanday qilib tozalashimizni yozing‼⌨️(Kod shaklida)" )

uchirish.clear()
print(f"Juda yaxshi💪🏻. Ana endi bizda nima hosil bo'lganini ko'ramiz🆓  Natija: {uchirish}")

tuugatish = """
📍List  metodlar darsni muvaffaqiyatli tugatganiz bilan tabriklayman🥳.
                                   &
                        O'qishlaringizga omad😇

"""
print(tuugatish)
print("Xayr🙋🏻‍") 

# Talim = ["maktab", "universitet", "Kolej", "Kitob"]
# print(f"Ta'lim ---> {Talim}")

# Oqish001 = Talim.copy()
# print(f"Ta'lim ---> {Talim}")
# print(f"O'qish ---> {Oqish001}")

# Talim.clear()
# print(f"Ta'lim ---> {Talim}")