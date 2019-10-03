print("Сидорова Олександра Сергіївна\nЛабораторна робота №1 \nВаріант 18 \nВизначення введеного символу \n")
while True:
    try:
        print("Введіть символ ")
        x = input()
        if x.isdigit():
            print("Ви ввели цифру")
        elif x.isalpha():
             print("Ви ввели букву")
        else:
             print("Ви ввели не букву або не цифру")

    except:
        print("Помилка")
        print("Для продовження введіть 1\nДля виходу введіть 0")
        a = input()
        while a != "1" and a != "0":
            print("Ви ввели некоректні дані")
            a = input()
        if a==0:
            break