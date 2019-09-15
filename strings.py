#!/usr/bin/python3

adi = 'Ömer Koçbil'

print(adi[3]) #cümlenin karakterlerinden oluşan bir liste gibi kabul ediyoruz
# adi[3] = 'l' hata verir, bu yok

soyadi = adi[5:] #bu iki işlem konumlama ve dilimleme aynı sadece listeler ile
print(soyadi)
print(len(soyadi))

for h in adi:
    print(h)

maas = 15
tutar = 1500.12
print('Maaşımı her ayın ', maas, '\'inde alırım', sep = '')
print('Maaşımı her ayın {1}\'inde {0} lira alırım' .format(tutar, maas))

cumle = 'python ömer'
print(cumle.upper())
print(cumle.lower())
print(cumle.title())

print(cumle.find('ömer'))
print(cumle.find('ömel'))

print(cumle.startswith('py'))
print(cumle.endswith('es'))

cumle2 = "Bugün hava çok güzel."
eposta = 'omer-95@hotmail.com'
print(cumle2.split())
kullanici, alan = eposta.split('@')
print(kullanici)
print(alan)

s = kullanici, alan
print(s)
eposta2 = '@'.join(s)        #dizilerin arasını ilk argüman ile birleştirir.
print(eposta2)

a = 'Beyaz atlı prens'
print(a.replace(' ', '_'))

a = '       ömer          '
print(a.strip())

i = '154'
print(i.isnumeric())
i = '12c45'
print(i.isnumeric())
i = '12.45'              # ondalık sayıları false olarak döndürür
print(i.isnumeric())






print('k' in 'Melike')
print('Melike Hatay\'dan geldi') #ters bölü, kendisinden sonraki karakterin 
                                 #cümle içinde asıl anlamında kullanılmasını 
                                 #sağlar
print('Bugün Fatih ile Melike oyun oynarken \
topları patladı')                                #satır sonuna sığmayanlar için
print('Bugün Fatih ile Melike oyun oynarken ' +  
      'topları patladı')                         #satır sonuna sığmayanlar için

dize = 'Kelimeler, kelimeler albayım \nBazı anlamlara gelmiyor'
print(dize)                              #\n bir alt satıra geçirir
dize2 = '''Tehlikeli oyunlar oynamak istiyor insan,
Bir yandan da kılına zarar gelsin istyemiyor. 
Küçük oyunlar istemiyorum albayım.
Kelimeler, kelimeler albayım, bazı anlamlara gelmiyor.

                                  Oğuz Atay'''
print(dize2)              #üç tırnak ile de uzun cümleleri yazabiliriz
# \t ifadesi de bir tab kadar boşluk koymak için kullanılır.

# Yukarıdaki gibi değişken ekleyebileceğimiz gibi cümlenin içine C'deki gibi de
#ekleyebiliriz. Bir de Python'ın özelliği format() ile ekleyebilriz.
print('Maaşımı her ayın %d\'inde alırım' % maas)
print('Maaşımı her ayın %d\'inde %0.2f lira alırım' % (maas, tutar))







