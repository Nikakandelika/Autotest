def task_1():
    values = [5, 2.4, 'home', [1, 2, 3, 4], True]
    for elem in range(len(values)):
        print(type(values[elem]))
task_1()

def task_2() -> str:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]
print(*(task_2()))
task_2()

def task_3(x: int) -> int:
    return x ** 2
print(task_3(2))




