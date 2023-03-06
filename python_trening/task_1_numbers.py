def test_passing():
    a = 2
    print (a, "относится к типу", type(a))

    b = 15.0001
    print(b, "относится к типу", type(b))

    c = 1+2j
    print(c, "Комплексное число? ", insinstance(c, complex))


print(6 + 2) # 8
print(6 - 2) # 4
print(6 * 2) # 12
print(6 / 2) # 3.0

print(7 / 2) # 3.5
print(7 // 2) # Получение целого числа от деления. Результат - 3

print(7 % 2) #

print(6 ** 2)