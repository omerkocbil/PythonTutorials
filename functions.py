#!/usr/bin/python3

def gelenSayiyaBesEkle(x):
    ''' Gelen Sayiya Beş Ekler ''' # Fonksiyon açıklaması
    y = x + 5
    return y

print(gelenSayiyaBesEkle(3))
help(gelenSayiyaBesEkle) #Fonksiyon açıklama satırını getirir

def bolum(bolunen, bolen):
    print(bolunen / bolen)

bolum(16, 2)
bolum(bolen=2, bolunen=16)

def cember(r):
    cevre = 2 * 3.14 * r
    alan = 3.14 * (r**2)
    return cevre, alan

cevre, alan = cember(3)
print(cevre)
print(alan)
