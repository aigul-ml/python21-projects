"""
Инкапсуляция 
"""

# Инкапсуляция - принцип ООП 
# 1. сокрытие данных (ограничение доступа к определенным методам и к определенным классам)
# 2. сбор всех необходимых для класса методов и атрибутов в "капсулу" (класс)


"""
Модификаторы доступа к атрибутам -- степени защиты
"""
# 1. public (публичный)
# 2. protected (защищенный)
# 3. private (приватный)
class A: 
    attr1 = 'public'
    _attr2 = 'protected'
    # _ --> with one underscore
    __attr3 = 'private'
    # __ --> two underscores for private attribute

A.attr1    # 'public'
A._attr2   # 'protected' 
# A.__attr3  # AttributeError --> type object 'A' has no attribute '__attr3' 
A._A__attr3 # 'private' 
print(A._A__attr3) 
# private 


"""
getter - получить 
setter - поставить новое значение 
"""
class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        # сохраним переменные в self
        self.__age = age 
        # self.__age - private 

    @property
    # встроенный декоратор, из метода превращает в атрибут
    def age(self): 
        return self.__age

    @age.setter
    def age(self, new_age): 
        # проверка на валидность введенного возраста
        if new_age < 120 and new_age > 0: 
            self.__age = new_age
        else: 
            raise Exception('Age cannot be less than 0 or more than 120.')
        
    
obj = Person("Nastya", 18)
# print(obj.__age)
# AttributeError: 'Person' object has no attribute '__age'
# print(obj.get_age())  --> was before using built-in decorator @property that converts method into attribute

# print(obj.get_age)   # because we used @property we call as attribute without paranthesis
# 18 
print(obj.age)
obj.age = 5
print(obj.age)
# 5 

