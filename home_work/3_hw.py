#1
a = 3
b = 3
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Печать запрещена")

#2
a = 235
b = 50
if (a-b) == 135 or (b-a) == 135:
    print("yes")
else:
    print("no")

#3
a = 0
if a in range(1, 3) or a == 12:
    print("зима")
elif a in range(3, 6):
    print("весна")
elif a in range(6, 9):
    print("лето")
elif a in range(9, 12):
    print("осень")
else:
    print("печать запрещена")

#4
a = 16
b = 15
c = 14
if a>10 and b>10 and c>10:
    print("yes")
else:
    print("no")


#5
a = [-3, -7, 25, 0, 1]
count = 0
for num in a:
    if num >= 0:
        count = count + 1
print(count)

#6
def arg(a, b):
    if a > 0 and b > 0:
        return a * 12 * 29 + b * 29
print(arg(1, 2))

