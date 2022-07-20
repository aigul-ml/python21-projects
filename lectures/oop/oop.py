from os import name


class SomeClass: 
    pass   # body of our Class

# example 1 
class A: 
    pass

a = A()

# а - экземпляр/объект класса -- instance/object of class A
# переменная а является объектом от класса А (после класса А обязательно указываем круглые скобки)

print(isinstance(a, A))
# True
# # метод isinstance принимает первым аргументом объект, который мы хотим проверить и вторым аргументом tuple - объекты могут принадлежать разным классам (к двум или более классам)

# проверяем является ли а объектом от класса А



# example 2
# встроенные классы 
# int, str, tuple, list, dict, bool, set, frozenset
a = 5 
print(type(a))
# <class 'int'>

b = 'makers'
print(type(b))
# <class 'str'>

c = [1, 2, 3, 4]
print(type(c))
# <class 'list'>

# example 3 
class Dog: 
    owner = 'Farhan'
    # name = 'Rex'
    # age = 3
    # аттрибуты класса
    # относится ко всем объектам, которые мы создаем от класса Dog

    def __init__(self, name, age) -> None:
        # def __init__ метод инициализатор - он срабатывает тогда, когда мы создаем объект от класса Dog
        # object of class Dog заходит в self - self говорит нам о том, что метод def __init__ применяется к нашему объекту и этот объект заходит вместо self
        

        self.name = name
        self.age = age
        # атрибуты экземпляров класса 
        # self - это и есть наш объект (первый аргумент)
        # атрибут экземпляра класса
        # self.name --> потому что мы обращаемся к самому объекту от класса  
        # аттрибуты экземпляров класса создаютсяв методе def __init__

    def bark(self):
        print('Gav-gav')

    def __str__(self) -> str:
        return f'{self.name} {self.age}'
        # возвращает объекты в str
        # method str при вызове объекта выводить нам читаемый объект в формате str

    def dog_info(self):
        return f'This is {self.name}, he is {self.age} years old.'

    def birthday(self, cake):
        self.age += 1
        self.cake = cake
        # возраст увеличивается на 1 
        return f'{self.name} is {self.age} now.'

    def friends(self, friend):
        self.friend = friend
        friend.friend = self
        # мы обращаемся к нашему friend и хотим, чтобы у него был такой же атрибут friend и чтобы у него был атрибут, который мы применили то есть self

    @classmethod
    def eat(cls):
        print('Nyam-nyam')

# print(dog1.name)
# обращаемся к атрибуту name через точку 

dog1 = Dog(name='Rex', age = 3)
# аргументы нашего объекта dog1
dog2 = Dog(name='Alisa', age=7)
print(dog1.name)
print(dog2.name)
# Rex
# Alisa

dog1.bark()
# вызываем метод bark() объекта dog1

print(dog1.birthday('vanilla'))
# Rex is 4 now.
print(dog1.age)
# 4

print(dog1.birthday('strawberry'))
print(dog1.cake)
# strawberry

dog1.friends(dog2)
print(dog1.friend.age)
# 7


# example 4
class Rectangle:

    default_color = 'red'

    def __init__(self, width, length) -> None:
        self.width = width 
        self.length = length

    def area(self):
        return self.width * self.length

rec1 = Rectangle(4, 6)
rec2 = Rectangle(7, 9)

print(rec1.area())
# 24

print(rec1.width)
# 4

print(rec1.default_color)
# red

rec2.default_color = 'yellow'
# переопределяем default_color 

print(rec2.default_color)
# yellow


# example 5 
class Car: 

    car_count = 0

    def __init__(self) -> None:
        Car.car_count += 1
        # обращаемся к самому классу Car на глобальном уровне и к атрибуту класса car_count и только тогда мы будем прибавлять 1, когда будем создавать новый объект

car1 = Car()
print(Car.car_count)
# обращаемся к самому классу Car, через класс обращаемся к атрибуту класса car_count
# 1

car2 = Car()
car3 = Car()
car4 = Car()
print(Car.car_count)
# 4

