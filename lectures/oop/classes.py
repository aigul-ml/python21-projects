class Person: 
    name = 'Anne'
    age = 12
    arms = 2 
    legs = 2 

    def walk(arg): 
        print(arg)
        print('I walk')

    def add_age(object): 
        object.age += 1 
person1 = Person()
person1.add_age()
print(person1.arms)
print(person1.walk())

Person.age = 17
print(Person.age)

person2 = Person()
print(person2.age)


class Person: 
    arms = 2 
    legs = 2 

    def __init__(self, name, age) -> None:    
        """
        функция, которая вызывается когда мы создаём объект от класса
        self - ссылка на созданный объект 
        """
        self.name = name         # мы добавляем в объект self новый атрибут name 
        self.age = age           # новый атрибут age 

    def add_age(object): 
        """
        функция, которая принимает объект и изменяет его возраст на 1 
        """
        object.age += 1 

    def __str__(self) -> str:
        """
        str - функция которая вызывается, когда мы оборачиваем объект в класс str или когда принтуем объект
        функция ___str___ ничего кроме self не принимает и обязательно должна возвращать строку
        """
        return self.name

person3 = Person('Anne', 50)
print(person3.age)   # returns age - int
print(person3)
person4 = Person('Lola', 30)
print(person4.age, person4.name)  # returns age and name 


"""
principles of oop - object-oriented programming 
"""
# наследование 
# инкапсуляция 
# полиморфизм
# абстракция 
# ассоциация 