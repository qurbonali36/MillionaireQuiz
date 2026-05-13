from functools import reduce


# 1. map and lambda

# narxlar_usd = [10, 25, 50, 100]

# uzb_som = list(map(lambda a: a*12500, narxlar_usd))
# print(uzb_som)

# 2. filter and lambda

# sozlar = ["olma", "nok", "banan", "gilos", "behi", "Shaftoli"]

# saralangan = list(filter(lambda b: len(b) >= 5, sozlar))

# print(saralangan)

# 3. List Comprehension 

# kub = [x**3 for x in range(1,11) if x%3==0]
# print(kub)

# # 4. zip

# id_raqamlar = [1, 2, 3]
# ismlar = ["Aziz", "Bekzod", "Sardor"]
# kasblar = ["Dasturchi", "Dizayner", "Menejer"]

# jamlangan = list(zip(id_raqamlar,ismlar,kasblar))

# print(jamlangan)

# 4. Ma'lumotlarni tozalash

# str_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", 20, "11.5"]

# int_nums = [int(float(x)) for x in str_nums]
# toza_toq_sonlar = [x*2 for x in int_nums if x%2 !=0]
# print("="*140)
# print(toza_toq_sonlar)
# print("="*140)

# 5.Baza yaratish

# xodimlar = ['Alice', 'Bob', 'Frank', 'Eve']
# maoshlar = [180_000, 99_000, 87_000, 110_000]
# kasblar = ['data scientist', 'project manager', 'backend developer', 'designer']

# baza = list(zip(xodimlar, maoshlar, kasblar))

# print(baza)
# print("="*140)

# 6.Elita xodimlarni saralash

# elita_xodims = list(filter(lambda a: a[1] >= 100_000, baza))

# print(elita_xodims)
# print("="*140)

# 7. Kompaniyaning umumiy byudjetini hisoblash

# umumiy_budjet = reduce(lambda a, b: a+b , maoshlar)

# print(f"Kompaniyaning umumiy budjeti {umumiy_budjet}-so'mni tashkil qiladi. ")
# print("="*140)

# # 7. Matn bilan ishlash

# text = "Call me Ishmael Some years ago never mind how long precisely having little or no money"

# splited_text = text.split()

# katta_uzun_sozlar = [x for x in splited_text if len(x) >= 5]
# print(list(map(lambda a: a.upper(), katta_uzun_sozlar)))


# 8.Tartibsiz Buyurtmalar Tahlili

mahsulotlar = ["  iphone 13 ", "apple WATCH", " macbook air  ", " iPad Pro ", "AirPods"]
narxlar_str = ["$900", "$400", "$1200", "$800", "$200"]
miqdorlar = [2, 5, 1, 0, 10,]

mahsulotlar = [mahsulot.strip().upper() for mahsulot in mahsulotlar ]
narxlar_int = list(map(lambda a: int(a.replace("$", "")), narxlar_str))


buyurtmalar1 = list(zip(mahsulotlar, narxlar_int, miqdorlar))
buyurtmalar = list(filter(lambda a: a[2] > 0, buyurtmalar1))
umumiy_narx = list(map(lambda a,b: a*b, narxlar_int,miqdorlar))
jami_daromad = reduce(lambda a,b: a+b, umumiy_narx)
chegirma = [buyurtma for buyurtma in buyurtmalar if buyurtma[1] > 500]
chegirma_qilingan =[
    (m, n * 0.9) if n > 500 else (m, n) 
    for m, n, miq in buyurtmalar
] 
print(f"""
	======================================================================================================================================
	Hozirgi vaqtda tushgan buyurtmalar: {buyurtmalar}
	======================================================================================================================================

	==============================================================================
	Har bir mahsulotni buyurtmasi bo'yicha umumiy narxi: {umumiy_narx}
	==============================================================================

	=============================================================
	Do'konni hozirgi holatiga ko'ra tushgan jami daromadi: ${jami_daromad}
	=============================================================

	================================================================================================================================================================================
	Do'konda hozir shu {chegirma_qilingan}  mahsulotlar uchun 10% chegirma qilindi.(Faqat 500$ qimatroq bo'lgan mahsulotlarga!)
	================================================================================================================================================================================

	""")