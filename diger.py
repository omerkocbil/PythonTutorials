#!/usr/bin/python3

x = 100

def f():
    global x
    x = 80
    print(x)

f()    
print(x)

m=[1, 2, 3]
print(dir([])) #nesnelerin özelliklerini getirir
print(dir(int))
print(dir(m)) #nesnelerin özellikleri böyle de gelir
print(m.clear.__doc__) #bu şekilde fonksiyonların ne işe yaradığına da
                       #bakabiliriz
