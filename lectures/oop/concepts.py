"===================Принципы ООП======================"
# Наследование
# Инкапсуляция
# Полиморфизм
# Абстракция
# Ассоциация

class A: 
    def method(self):
        print('method in class A')

obj_a = A()
obj_a.method()   # method in class A 

class B(A):   
    """"""
obj_b = B()
obj_b.method()   # method in class A 


# super() функция, которая позволяет обратиться к родительскому классу и вызвать определенные методы или аттрибуты 

class A: 
    def range(self, n): 
        return list(range(0, n+1))

class B(A): 
    def range(self):
        # через super() мы обращаемся к методу родительского класса
        return super().range(10)