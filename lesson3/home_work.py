# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.array = x*y
    def __add__(self, other):
        return self.array + other.array
    def __sub__(self, other):
        return self.array - other.array
    def __eq__(self, other):
        return self.array == other.array
    def __ne__(self, other):
        return self.array != other.array
    def __gt__(self, other):
        return self.array > other.array
    def __lt__(self, other):
        return self.array < other.array
    def __len__(self):
        return (self.x + self.y)*2

rectangle1 = Rectangle(2,3)
rectangle2 = Rectangle(20, 30)

print(rectangle1 + rectangle2)
print(rectangle1 - rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 != rectangle2)
print(rectangle1 > rectangle2)
print(rectangle1 < rectangle2)
print(len(rectangle1))
print(len(rectangle2))

# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Cinderella(Human):
    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self.size = size
    def __str__(self):
        return str(self.__dict__)

class Prince(Human):
    def __init__(self, name: str, age: int, shoes_size: int):
        super().__init__(name, age)
        self.shoes_size = shoes_size

    def find_cinderella(self, cinderellas_list: list[Cinderella]):
        for cinderella in cinderellas_list:
            if cinderella.size == self.shoes_size:
                print(cinderella)
                break

cinderellas_list: list[Cinderella] = [
    Cinderella('Olha', 16, 32),
    Cinderella('Maria', 21, 36),
    Cinderella('Viktoria', 24, 34),
    Cinderella('Yulia', 19, 33),
]
prince = Prince('Mike', 26, 34)
prince.find_cinderella(cinderellas_list)

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають
#   є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
# Приклад:
#   Main.add(Magazine('Magazine1'))
#   Main.add(Book('Book1'))
#   Main.add(Magazine('Magazine3'))
#   Main.add(Magazine('Magazine2'))
#   Main.add(Book('Book2'))
#
#   Main.show_all_magazines()
#   print('-' * 40)
#   Main.show_all_books()
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

from abc import ABC, abstractclassmethod

class Printable(ABC):
    @abstractclassmethod
    def print(self):
        pass

class Magazine(Printable):
    def __init__(self, name: str):
        self._name = name
    def print(self):
        print(self._name)

class Books(Printable):
    def __init__(self, name: str):
        self._name = name
    def print(self):
        print(self._name)

class Main:
    printable_list: list[Printable] = []
    @classmethod
    def add(cls, new_item: Printable):
        if isinstance(new_item, (Books, Magazine)):
            cls.printable_list.append(new_item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Books):
                item.print()

Main.add(Magazine('magaz_1'))
Main.add(Magazine('magaz_2'))
Main.add(Magazine('magaz_3'))
Main.add(Magazine('magaz_4'))
Main.add(Magazine('magaz_5'))

Main.add(Books('book_1'))
Main.add(Books('book_2'))
Main.add(Books('book_3'))
Main.add(Books('book_4'))

Main.add(prince)

print('*'*50)
Main.show_all_magazines()
print('*'*50)
Main.show_all_books()
print('*'*50)
print(Main.printable_list)

