# -*- coding: utf-8 -*-

#Range fonksiyonu -> range(başlangıç degeri,bitiş değeri(Dahil değil))

print(*range(0,10))

liste1=list(range(0,10))

print(*range(5,15))

print(*range(14))

print(*range(0,10,2))

print(*range(10,0))  #çalışmaz

print(*range(10,0,-1)) 

for i in range(0,15):
    print(i)
    
for k in range(0,10):
    print("* "*k)

print("")
        
for k in range(10,0,-1):
    print("* "*k)