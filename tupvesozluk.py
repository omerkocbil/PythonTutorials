#!/usr/bin/python3
cakmaSozluk = [('adhere', 'yapışmak'), ('bald', 'dazlak, kel')] #sözlük gibi kullana
                                                           #bileceğimiz yapı
sozluk = {'adhere':'yapışmak', 'bald':'dazlak, kel'} #sözlük yapısı
print(sozluk['bald'])
print(sozluk)                  #bizim verdiğimiz ile aynı sırada gelmez

sozluk['page'] = 'sayfa'       #sonradan değer ekleyebiliriz
print(sozluk)
print('title' in sozluk)

keys = sozluk.keys()           #anahtar kelimeleri liste olarak verir
print(keys)

sort = sorted(sozluk)
sort2 = sorted(sozluk.keys())  #ikisi de aynı işlevi görür
print(sort)

values = sozluk.values()       #değerleri liste olarak verir
print(values)

items = sozluk.items()         #key-value lar tüpün içinde olan bir liste verir
print(items)

deger = sozluk.get('page')
deger2 = sozluk.get('title')   #get() in farkı eğer o key yoksa None döndürür
deger3 = sozluk.get('title', 'Sözlükte bulunamadı') #2. arg verirsek boş yerine 
                                                    #onu döndürür
print(deger)
print(deger2)
print(deger3)

silinen = sozluk.pop('page')   #silerken değerini de döndürür
print(silinen)
del sozluk['adhere']           #del Python nesnesini bellekten silmek için
                               #kullanılır. Bir değişkeni de bu şekilde sileriz
print(sozluk)

kelimeler = sozluk             #listeler ile aynı. takma ad görevi görür
kelimeler['car'] = 'araba'
print(sozluk)
kopyaSozluk = sozluk.copy()    #sözlük ün kopyasını alır
kopyaSozluk.pop('car')
print(sozluk)

guncelBilgiler = {'car':'at', 'page':'sayfa'}
sozluk.update(guncelBilgiler)  #parametre ile sozluk arasında aynı key varsa
                               #günceller yoksa ekler
print(sozluk)

sozluk8 = {'1':topla, '2':enBuyukVeEnKucuk}  #değer olarak fonkda verebiliriz
print(sozluk8['1'])                          #ama atarken parantez yok 
print(sozluk8['1'](5, 7))                    #çağırırken parametreler atanacak








degerler = (12.5, 'ali', 5) #tüp yapısı #liste gibidirler ama değiştirilemezler
kalkis, varis, mola = '12:30', '20:00', 4       #iki şekilde de kullanılabilir
(kalkis, varis, mola) = ('12:30', '20:00', 4)   #iki şekilde de kullanılabilir
#yukarıdaki gibi olunca tek başına kalkis değiştirlebilir çünkü o tüpün içi
#listeler ile count() ve index() ortak fonksiyonlarıdır

def topla(*sayilar):     #başına * koyunca tüp oluyor sayısız parametre almasını
                         #sağlıyor. Javadaki int sayilar... gibi
    toplam = 0
    for i in sayilar:
        toplam = toplam + i
    return toplam

print(topla(2, 3))
print(topla(2, 3, 4))

def enBuyukVeEnKucuk(*sayilar):
    return max(sayilar), min(sayilar)

print(enBuyukVeEnKucuk(45, 97, 3, 120, 56))






