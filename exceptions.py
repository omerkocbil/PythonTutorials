#!/usr/bin/python3

yas = input("Lütfen yaşınızı giriniz: ")

try:
    yas = int(yas)
    print('Üç yıl sonra', yas + 3, "yaşında olacaksınız")
except:
    print("Sayı değer girmediniz.")


for i in ["5", (5, 4), 9, 'm', "6"]:
    try:
        print(int(i) * 2)
    except TypeError as hata1:
        print("Tip hatası yakalandı:", hata1.args[0])
    except ValueError as hata2:
        print("Değer hatası yakalandı:", hata2.args[0])


def karekok(x):
    if x < 0:
        raise ValueError('Geçersiz Değer: karekökü alınacak sayı negatif olamaz')
        #yukarıdaki ifade exception fırlatmak gibidir ama tanımlanmış sınıflarla
    return x**0.5

# print(karekok(-5)) bu çalışıyor hata vermesin output da diye comment ledik


class GecersizDeger(Exception):    #kendi exception ını oluşturma
    
    def __init__(self, hataIletisi):
        self.hata = hataIletisi

def karekok2(x):
    if x < 0:
        raise GecersizDeger('Geçersiz Değer: karekökü alınacak sayı negatif olamaz')
    return x**0.5

try:
    print(karekok2(-5))
except GecersizDeger as hatam:
    print(hatam)


try:
    karekok2(25)
except:
    print("Bir hata yakalandı")
else:                                   #hata yakalanmaz ise bu blok işletilir 
                                        #finally gibi değil
    print("Herhangi bir hata yakalanmadı")


try:
    karekok2(-9)
except:
    print("Bir hata yakalandı")
else:
    print("Herhangi bir hata yakalanmadı")
finally:                                #hata yakalansa da yakalanmasa da bu
                                        #blok işletilir
    print("Bu son blok her zaman işletilir")













        
