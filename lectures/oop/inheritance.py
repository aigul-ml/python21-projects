"Наследование - принцип ООП, где мы можем в дочернем классе унаследовать, переопределять и использовать все аттрибуты и методы родительского класса"

class A:
    def method(self):
        print("method in class A")

obj_a = A()
obj_a.method() # 'method in class A'

class B(A):
    """Наследовали все методы и аттрибуты у класса А"""

obj_b = B()
obj_b.method() # 'method in class A'

"class A - родительский класс"
"class B - дочерний класс"

class C(A):
    """Наследовали все методы и аттрибуты у класса A и переопределили метод method"""

    def method(self):
        print("method in class C")

obj_a = A()
obj_a.method() # 'method in class A'

obj_c = C()
obj_c.method() # 'method in class C'

"Переопределение - даем то же название, но другое значение"

"super() - функция, которая позволяет обратиться к родительскому классу и вызвать определенные методы или аттрибуты"
class A:
    def my_range(self, n):
        return list(range(0, n+1))

class B(A):
    def my_range(self):
        # через super мы обращаемся к методу родительского класса
        return super().my_range(10)

obj_a = A()
obj_a.my_range(3) # [0,1,2,3]

obj_b = B()
obj_b.my_range() # [0,1,2,3,4,5,6,7,8,9,10]

"================= множественное наследование ==============="
# наследование от 2 и более классов
class A: 
    a = 'a'

class B: 
    b = 'b'

class C(A, B): 
    """ наследовались от 2 классов А и В """
    c = 'c'
obj_c = C()
obj_c.a # 'a' 
obj_c.b # 'b' 
obj_c.c # 'c'


"""
Проблемы множественного наследования 
"""
# 1. проблема ромба - решенная проблема (с помощью MRO) --> method resolution order
class A: ...

class B(A): ...

class C(A): ...

class D(B, C): ...
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


"""
2. Проблема перекрёстного наследования - нерешенная проблема 
"""
class A: ...
class B: ...

class C(A, B): ...
class D(B, A): ...

# class E(C, D): ...
# cannot create method resolution order (MRO) for bases A, B



"=================Виды наследования==============="
# одиночное наследование
# множественное наследование
# многоуровневое наследование
# иерархическое наследование
# гибридное наследование