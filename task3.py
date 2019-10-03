print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nОбчислення функції в залежності від значення введеної змінної \n")
from math import sin
while True:
    try:
        print("Введіть х ")
        x = float(input())
        if x<=3:
           print( x**2 +3*x+9)
        else:
           print(sin(x)/(x**2-9))
    except:
        print("Помилка")
        print("Для продовження введіть 1\nДля виходу введіть 0")
        a = input()
        while a != "1" and a != "0":
            print("Ви ввели некоректні дані")
            a = input()
        if a==0:
            break