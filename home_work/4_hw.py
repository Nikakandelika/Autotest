#1
class Rectangle:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    def Square(self):
        return(self.width * self.height)
    def Perimeter(self):
        return(2*(self.width + self.height))

huh = Rectangle(2, 5)
huh_2 = Rectangle(3, 6)
huh_3 = Rectangle(6, 2)

print(huh.Square())
print(huh_2.Square())
print(huh_3.Square())
print(huh.Perimeter())
print(huh_2.Perimeter())
print(huh_3.Perimeter())

#2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b

lol = Math(3, 7)

print(lol.multiplication())

#3
class Demoqa:
    def __init__(self, text, type="Кнопка", locator=""):
        self.text = text
        self.type = type
        self.locator = locator
    def button(self):
        return f'Клик по кнопке {self.text}'

textbox = Demoqa("Текст бокc")
print(textbox.button())

checkbox = Demoqa("Чек бокс")
print(checkbox.button())

radio_button = Demoqa("Радио кнопка")
print(radio_button.button())

webtables = Demoqa("Веб таблицы")
print(webtables.button())

buttons = Demoqa("Кнопки")
print(buttons.button())

links = Demoqa("Ссылки")
print(links.button())

brokenlinks = Demoqa("Битые ссылки")
print(brokenlinks.button())
