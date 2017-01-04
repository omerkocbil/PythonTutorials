#!/usr/bin/python3

x = 8

if(x > 5):
    print("Sayı 5'ten büyük")
elif(x > 10):
    print("Sayı 10'dan büyük")
else:
    print("Sayı 5'ten küçük")

i = 1

while(i <= 5):
    if(i == 3):
        break
    elif(i == 2):
        i = i + 2
        continue
    print(i)
    i += 1

sayac = 0
sayi = 2

while(sayac != 2):
    if(sayi > 5):
        print("Ooo sayı büyükmüş")
    sayi = sayi * 2    
    sayac = sayac + 1
else:
    print("Ooo sayı küçükmüş")
