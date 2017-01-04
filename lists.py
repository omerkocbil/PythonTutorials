#!/usr/bin/python3

ogrenciler = [] #liste tanımı

ogrenciler.append("Ömer Koçbil")
ogrenciler.append("Cem Dırman")
ogrenciler.append("Ahmet Emre Demirşen")

print(ogrenciler[0])

ogrenciler[2] = 'Ömer Yazıcı'

print(ogrenciler)

print(len(ogrenciler))

kuruyemisler = ["fındık", "fıstık", "badem"]
print(kuruyemisler)

print(kuruyemisler[-1])
print(kuruyemisler[-2])

meyveler = ["elma", "portakal", "kivi", "armut"]
sevdigimMeyve = 'karpuz'
varMi = sevdigimMeyve in meyveler

print(varMi)

for meyve in meyveler:
    print(meyve)

for i in range(5):
    print(i)

for u in range(0, 24, 3):
    print(u)

print(meyveler.pop()) #elemanı çıkarıp geri dönderir
print(meyveler.remove('elma')) #geri döndermiyor bu
print(meyveler.count('portakal')) #portakaldan kaç tane olduğunu sayar
print(meyveler.index('kivi')) #kivinin index ini verir

meyveler.reverse() #diziyi ters çevirir
print(meyveler)
meyveler.reverse()

print(sorted(meyveler)) #diziyi sıralar ama dizi değişmez
print(meyveler)
print(meyveler.sort()) #diziyi sıralar ve yapısı değişir
print(meyveler)

meyveler.insert(1, "kavun")
print(meyveler)

meyveler.extend([3, 7])
print(meyveler)
meyveler = meyveler + kuruyemisler
print(meyveler)
meyveler = meyveler * 2
print(meyveler)

myv = meyveler #bu işlem nesne ataması yapmaz, meyveler listesini myv adıyla da
               #çağırmama yarar. myv de yapılan değişiklikler meyveleri de etklr
myv.insert(0, "Ali")
print(meyveler)

myv2 = []
for u in meyveler: #nesne kopyalaması yapmak için bunu kullanabiliriz
    myv2.append(u)

print(myv2)

print(myv2[1:3]) #indeksi 1 ve 2 olan elemanlar alınır
print(myv2[:2])  #indeksi 0 ve 1 olan elemanlar alınır
print(myv2[3:])  #indeksi 3 ten sona kadar olan elemanlar alınır
print(myv2[:])   #bütün elemanlar alınır

myv3 = meyveler[:] #nesne kopyalaması yapmak için bunu da kullanabiliriz
myv3.insert(0, "Ömer")
print(meyveler)

















