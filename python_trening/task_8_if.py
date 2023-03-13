#1
num = 3
if num >= 0:
    print("Число больше либо равно нулю")
else:
    print("Число отрицательное")


#2
str_1 = "test"
str_2 = "test1"
if str_1 in str_2:
    print("Верно")
else:
    print("Неверно")

#3
num_float = 3.4
if num_float > 0:
    print("Положительное число")
elif num_float == 0:
    print("Ноль")
else:
    print("Число отрицательное")

#4
permit_print = True
if num > 0 and permit_print:
    print("num - положительное число")
elif not permit_print:
    print("Печать запрещена")

#5
a = 10
if a in range(1, 5):
    print("Бакалавр")
elif a in range(5, 7):
    print("Магистр")
elif a in range(7, 10):
    print("Аспирант")
else:
    print("Печать запрещена")