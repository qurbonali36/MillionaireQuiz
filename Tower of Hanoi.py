# TOWER OF HANOI
# 3 TA DISKNI A USTUNDA C USTUNGA KO'CHIRISH,B YORDAMCHI USTUN ORQALI
# QOIDALAR:
# 1)BIR VAQTDA FAQAT 1 TA DISK KO'CHADI
# 2)KATTA DISK KICHIK DISK USTIGA QO'YILMAYDI
# n=disklar soni
# from_rod=qayerdan ko'chiryapmiz
# to_rod=qayerga ko'chiryapmiz
# aux_rod=yordamchi ustun

def Tower_Of_Hanoi(n,from_rod,to_rod,aux_rod):
    if n==1:
        print("Move disk 1 from_rod",from_rod,"to_rod",to_rod)
        return
    Tower_Of_Hanoi(n-1,from_rod,aux_rod,to_rod)
    print("Move disk",n,"from_rod",from_rod,"to_rod",to_rod)
    Tower_Of_Hanoi(n-1,aux_rod,to_rod,from_rod)
n=int(input("Enter the number of disks you want to move: "))
print(Tower_Of_Hanoi(n,'A','C','B'))
