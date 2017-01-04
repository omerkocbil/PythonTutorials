#!/usr/bin/python3

import sys, random, string

def maxOfThree(sayi1, sayi2, sayi3):
    max = sayi1
    if (sayi2 > sayi1):
        if (sayi2 > sayi3):
            max = sayi2
        else:
            max = sayi3
    elif (sayi3 > sayi1):
        max = sayi3

    return max

print(maxOfThree(12, 8, 9))

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def drawTicTacToe():
    print(" --- --- --- ")
    for i in range(3):
        for j in range(4):
            sys.stdout.write("|   ")       #satır atlamadan yazdırmak için

        print()
        print(" --- --- --- ")

drawTicTacToe()

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def guessingGameOne():
    rasgele = random.randint(1, 9)
    sayi = -1
    sayac = 0
    while(sayi != rasgele):
        sayi = input("Lütfen 1-9 arasında bir sayı giriniz ya da çıkmak için 'exit' yazınız: ")
        if (sayi == "exit"):
            print("Oyun bitti")
            break
        if(not sayi.isnumeric()):
            print("Girdiğiniz değer sayı ya da 'exit' değil")
            continue
        sayi = int(sayi)
        sayac = sayac + 1
        if(sayi == rasgele):
            print("Tebrikler", sayac, "adımda kazandınız!!!")
        else:
            print("Olmadı, haydi bir daha deneyelim")

#guessingGameOne()

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def guessingGameTwo():
    ''' 0 ile 100 arasındaki sayılar için '''
    deger = 50
    degerler = [0, 50]
    alcakMi, yuksekMi = False, False 
    sayi = input("Tuttuğun sayı " + str(deger) + " mi: ")
    while(True):
        if(sayi == "doğru"):
            print("I'm the best :)")
            break
        elif(sayi == "alçak"):
            if(yuksekMi):
                gercekDeger = 0
                i = -1
                while(True):
                    if(degerler[i] > deger):
                        gercekDeger = degerler[i]
                        break
                    i = i - 1
                deger = deger + (gercekDeger - deger) // 2
            else:
                deger = deger + (100 - deger) // 2
            alcakMi = True
        elif(sayi == "yüksek"):
            if(alcakMi):
                gercekDeger = 0
                i = -1
                while(True):
                    if(degerler[i] < deger):
                        gercekDeger = degerler[i]
                        break
                    i = i - 1
                deger = deger - (deger - gercekDeger) // 2
            else:
                deger = deger // 2
            yuksekMi = True
        else:
            print("Lütfen sadece 'doğru', 'alçak' ya da 'yüksek' giriniz")
            continue

        degerler.append(deger)
        print(degerler)
        sayi = input("Tuttuğun sayı " + str(deger) + ' mi: ')

#guessingGameTwo()

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def rockPaperScissors():
    computerPoints, userPoints = 0, 0
    while(True):
        computer = random.choice(['rock', 'paper', 'scissors'])
        user = input("Please enter 'rock', 'paper' or 'scissors'. Or enter 'exit' for exit : ")
        print("Computer's choice is:", computer)
        if(user == 'exit'):
            break
        elif(user == computer):
            print("Tie!!!")
        elif((computer == 'rock') and (user == 'scissors')):
            print("Computer win!!!")
            computerPoints = computerPoints +1
        elif((computer == 'paper') and (user == 'scissors')):
            print("User win!!!")
            userPoints = userPoints +1
        elif((computer == 'rock') and (user == 'paper')):
            print("User win!!!")
            userPoints = userPoints +1
        elif((computer == 'scissors') and (user == 'paper')):
            print("Computer win!!!")
            computerPoints = computerPoints +1
        elif((computer == 'paper') and (user == 'rock')):
            print("Computer win!!!")
            computerPoints = computerPoints +1
        elif((computer == 'scissors') and (user == 'rock')):
            print("User win!!!")
            userPoints = userPoints +1
        else:
            print("Please don't enter another word")
        print("Computer:", computerPoints, "  User:", userPoints)

    print("Game is over!!!", "  Computer:", computerPoints, "  User:", userPoints)
    
#rockPaperScissors()

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def commonElements(list1, list2):
    list3 = []
    for i in list1:
        if i in list2:
            if(not i in list3):
                list3.append(i)
    print("Common Elements:")
    for j in list3:
        print(j)

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
commonElements(list1, list2)

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def asalSayiBul(sayi):
    kopya = sayi - 1
    asalMi = True
    for i in range(sayi):
        if(sayi == 2):
            break
        if(kopya == 1):
            break
        if(sayi % kopya == 0):
            asalMi = False
            break
        kopya = kopya - 1
    if(asalMi):
        print(sayi, "sayısı asaldır")
    else:
        print(sayi, "sayısı asal değildir")

asalSayiBul(1453)

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def fibonacciNumbers(seri):
    ilkSayi, ikinciSayi = 0, 1
    kesinSayi = ilkSayi + ikinciSayi
    print("Fibonacci Serisi:")
    print(ikinciSayi)
    print(kesinSayi)
    for i in range(seri-2):
        ilkSayi = ikinciSayi
        ikinciSayi = kesinSayi
        kesinSayi = ilkSayi + ikinciSayi
        print(kesinSayi)

fibonacciNumbers(60)

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def removeDuplicates(list):
    list2 = []
    for i in list:
        if(not i in list2):
            list2.append(i)
            print(i)

list = [1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 55, 55, 89]
removeDuplicates(list)

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def reverseWordOrder(cumle):
    list = cumle.split(' ')
    list.reverse()                  #direk ters çeviri ve kendisine atar
    cumle = " ".join(list)
    print(cumle)

cumle = 'Python is funny'
reverseWordOrder(cumle)

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def generatePassword(weakness, length):
    lowerAlphabetList = string.ascii_lowercase   #(k)alfabeyi listeye çevirir
    upperAlphabetList = string.ascii_uppercase   #(B)alfabeyi listeye çevirir
    numberList = string.digits                   #0-9 sayıları listeye çevirir
    symbolList = string.punctuation              #sembolleri listeye çevirir
    passwordList = []
    if(weakness == "weak"):
        for i in range(length):
            if(i >= length * (3 / 4)):
                passwordList.append(random.choice(upperAlphabetList))
            else:
                passwordList.append(random.choice(lowerAlphabetList))
    elif(weakness == "average"):
        for i in range(length):
            if(i >= length * (3 / 4)):
                passwordList.append(random.choice(numberList))
            elif(i >= length * (2 / 4)):
                passwordList.append(random.choice(upperAlphabetList))
            else:
                passwordList.append(random.choice(lowerAlphabetList))
    elif(weakness == "strong"):
        for i in range(length):
            if(i >= length * (3 / 4)):
                passwordList.append(random.choice(symbolList))
            elif(i >= length * (2 / 4)):
                passwordList.append(random.choice(numberList))
            elif(i >= length * (1 / 4)):
                passwordList.append(random.choice(upperAlphabetList))
            else:
                passwordList.append(random.choice(lowerAlphabetList))
                
    random.shuffle(passwordList)        #listeyi karıştırır, ='lemeye gerek yok
    password = ''.join(passwordList)
    return password

password = generatePassword('strong', 16)
print(password)

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()

def cowsAndBullsGame():
    computer = random.randint(1000, 9999)
    print("Welcome to the Cows and Bulls Game!")
    cows, bulls = 0, 0
    while(True):
        sayi = input("Enter an number: ")
        for i in range(4):
            if(sayi[i] == str(computer)[i]):
                cows = cows + 1
            elif(sayi[i] in str(computer)):
                bulls = bulls + 1
        if(cows == 4):
            print("Game is over, you won!!!")
            break
        print(cows, "cows,", bulls, "bulls")
        cows = 0
        bulls = 0

cowsAndBullsGame()

print()
print("-----BİR SONRAKİ ALIŞTIRMA-----")
print()










