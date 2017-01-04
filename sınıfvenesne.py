#!/usr/bin/python3

class Vektor():
    """Bu bir vektör nesnesidir"""

A = Vektor()

print(A)
print(A.__doc__)       #nesne ile ilgili açıklama

A.y = 8                #bu şekilde özelliği olmasa da atayabiliriz
A.x = 6 
print(A.x)             #hata vermez sonuç 6 gelir

class Vektor2():
    """Bu bir vektör nesnesidir"""

    def __init__(self, x, y):    #sınıf içindeki her fonk için ilk parametrenin
                                 #self olması gerekiyor.
        print("Bir Vektor2 nesnesi oluşturuldu")


A2 = Vektor2(6,8)

# print(A2.x) çalışmaz erişemeyiz

class Vektor3():
    """Bu bir vektör nesnesidir"""

    def __init__(self, x, y):
        self.x = x               #bu şekilde tanımlarsak erişebiliriz
        self.y = y               #bu şekilde tanımlarsak erişebiliriz

    def vektorunBoyu(self):      #self i yazmazsak dışarıdan erişemeyiz
        boy = (self.x**2 + self.y**2) ** 0.5
        return boy

    def __repr__(self):           #bu method nesnenin yazdırınca açıklaması için
        return ("%di + %dj" % (self.x, self.y))

    def __add__(self, vektorNesnesi):    #operator overloading for +
        return Vektor3(self.x + vektorNesnesi.x, self.y + vektorNesnesi.y)

    def __gt__(self, vektorNesnesi):       #operator overloading for > and <
        if(self.vektorunBoyu() > vektorNesnesi.vektorunBoyu()):
            return True
        else:
            return False

        
A3 = Vektor3(6,8)

print(A3.vektorunBoyu())

A3.x = 24
print(A3.vektorunBoyu())

print(A3)                        #__repr__ metodu devreye girecek

B = Vektor3(5, 2)
C = Vektor3(1, 7)
D = B + C
print(D)

isGreat = B > C
isSmall = D < A3
print(isGreat)
print(isSmall)


class Ebeveyn:

    def anneninSacRengi(self):
        return 'sarı'

    def babaninGozRengi(self):
        return 'mavi'


class Cocuk(Ebeveyn):

    def __init__(self, adi = ''):
        self.adi = adi

    def sacRengi(self):
        print(self.adi, "in saç rengi muhtemelen", self.anneninSacRengi(), "olacaktır")

    def babaninGozRengi(self):             #method overriding
        print("Şimdi bunu bilmiyoruz")


omer = Cocuk('Ömer')
omer.sacRengi()

print(omer.babaninGozRengi())


class Amca:

    def amcaninSacTipi(self):
        return "kıvırcık"


class Cocuk2(Ebeveyn, Amca):
    def __init__(self, adi = ''):
        self.adi = adi

    def sacRengi(self):
        print(self.adi, "in saç rengi muhtemelen", self.anneninSacRengi(), "olacaktır")

    def saci(self):
        print(self.adi, "in saçı", self.anneninSacRengi(), 've', self.amcaninSacTipi(), "olabilir.")


omer2 = Cocuk2("Ömer")
omer2.saci()















    




