# -*- coding: utf-8 -*-

a=45
b=34

secim=int(input("Toplama (1), Çıkarma(2), Çarpma(3), Bölme(4)\n İşlem Seçiniz:"))


if(secim==1):
    print(a+b)
elif(secim==2):
    print(a-b)
elif(secim==3):
    print(a*b)
elif(secim==4):
    print(a/b)
else:
    print("Hatalı seçim")