"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
class Circle:
    color = 'blue'
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius 

    def get_area(self): 
        return Circle.pi * pow(self.radius, 2)

circle = Circle(2)
circle.color = 'red'
print(circle.color)
print(circle.get_area())

"""
2) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""

class Phone:
    def __init__(self, name, surname, phone) -> None:
        self.name = name
        self.surname = surname 
        self.phone = phone

    def get_info(self): 
        print(f'Контакт: {self.name} {self.surname}, телефон: {self.phone}')

contact = Phone('Ivan', 'Petrov', +996555777888)
contact.get_info()

"""
3) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""

class Person: 
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age 

    def display(self): 
        return f'name: {self.name}, age: {self.age}'

class Student(Person):
    def __init__(self, name, age, faculty) -> None:
        super().__init__(name, age)
        self.faculty = faculty
    
    def display(self):
        return super().display()
    
    def display_student(self): 
        person_display = super().display()
        return f'{person_display}, faculty: {self.faculty}'

obj_student = Student('Rick', 23, 'science')
print(obj_student.display())
print(obj_student.display_student)

"""
4) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""
class Dog:
    def voice(self): 
        print("Гав")

class Cat: 
    def voice(self): 
        print("Мяу")

barsik = Cat()
rex = Dog()

def to_pet(animal): 
    animal.voice()

to_pet(barsik)
to_pet(rex)


"""
5) Объявите класс Car, в котором будет приватный атрибут экземпляра класса speed.
Затем, определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, который возвращает значение скорости.
Создайте экземпляр в переменной car1 класса Car и вызовите все методы.
"""

class Car: 
    __speed = 0

    def set_speed(self, speed):
        self.__speed = speed

    def show_speed(self): 
        return self.__speed
    
car1 = Car()

print(car1.show_speed)
car1.set_speed(20)
print(car1.show_speed)