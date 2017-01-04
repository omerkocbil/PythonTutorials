#!/usr/bin/python3

import module1      #önce terminal su yaz şifre gir sonra cd /usr/bin yaz sonra
                    #touch dosyaAdi.py yaz. sonra gedit dosyaAdi.py yaz sonra
                    #bu modüle istediğin şeyler, gir değişken işlev aynı python
                    #programlıyormuş gibi. sonra bu şekilde çağır kullan. direk
                    #izin vermiyor o yüzden terminalden yapıyoruz.
from module1 import renkler                     #1
from module1 import *                           #2
from module1 import renkler as anaRenkler       #3
import module2
from module2 import karekokAl

import time         #hazır zaman modülü

import random       #hazır random modülü

import os           #hazır işletim sistemi modülü

print(module1.adi)  #moduleAdi. değişken,liste şeklinde çağrılır
print(renkler[2])   #(1) yukarıdaki gibi tanımlarsak direk de kullanabiliriz
print(soyadi)       #(2) yukarıdaki gibi tanımlarsak hepsini direk kullanabilriz
print(anaRenkler)   #(3) yukarıdaki gibi tanımlarsak farklı isimde kullanabilriz

print(module2.karekokAl(5))
print(karekokAl(25))

print(dir(module2)) #modülümüzün hangi işlev değişkenlere sahip olduğunu görürüz

print(time.time())       #1970 den bu yana geçen saniye sayısı
print(time.localtime())  #9 elemanlı tüp döndürür. yıl, ay, gün, saat, dakika,
                         #saniye, haftanın günü(0-6), yılın kaçıncı günü, 
                         #ileri saat uygulaması
print(time.ctime())
zaman = time.localtime()
print(zaman[2], '/', zaman[1], '/', zaman[0], ' ', zaman[3], ':', zaman[4], sep='')
epoch = time.mktime((2016, 7, 15, 21, 0, 0, 4, 185, 1)) #bütün değerler verilip
                                                        #saniye alınabilir
print(epoch)

time.sleep(2)            #2 saniye bekletir programı

print(random.random())   #0-1 arasında rasgele sayı üretir
print(random.randrange(50, 95))   #belli iki sayı arasında ragele sayı üretir 
print(random.choice(['maça', 'sinek', 'kupa', 'karo']))  #rasgele seçim yapar
print(random.choice('ABCDEF12345'))                      #rasgele seçim yapar

print(os.name)           #işletim sisteminin adı
print(os.uname())        #işletim sisteminin çekirdeğine ait ayrıntılı bilgi

for i in os.environ:     #çevre değişkenleri listesi
    print(i, ":", os.environ[i])

print(os.path.exists('/home/jan/Downloads'))   #dosya var mı yok mu
print(os.path.exists('/home/jan/Omer'))
print(os.path.isfile('/home/jan/Downloads'))   #bu bir dosya mı
print(os.path.isdir('/home/jan/Downloads'))    #bu bir klasör mü
print(os.listdir('/home/jan/PythonProjects'))  #klasörün içindekileri listeler



















