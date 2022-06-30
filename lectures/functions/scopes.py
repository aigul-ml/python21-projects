"================ Области видимости и пространства имен =================="
locals()  # - возвращает словарь со всеми локальными переменными
globals()  # - возвращает словарь со всеми глобальными переменными

# LEGB - local, enclosed, global, build-in

"Build-in"  # - встроенное пространство имен (все втроенные переменные (print, input, sum, max, min, len, abs, int, str, dict ...))

"Global" # - глобальное пространство имен (все переменные внутри файла, которые создали мы) 
# чтобы узнать, что находится в глобальном пространстве, можно использовать функцию globals

"Enclosed" # - пространство находящееся между двумя пространствами

"Local" # - какое-то закрытое пространство

# example
a = 10
d = 7

def func(b, c):
    # локальное пространство
    a = 5
    print(locals())
    # {'b': 5, 'c': 2, 'a': 5}
# func(5,2)

def func():
    # enclosed пространство
    a = "func"
    def inner_func():
        # local пространство
        a = "inner_func"
        print(locals()) # {'a': 'inner_func'}
    inner_func()
    print(locals()) # {'a': 'func', 'inner_func': <function func.<locals>.inner_func at 0x7fa171fa8d30>}

# func()

эртай = 'алиби'

def func():
    nastya = 'python21'
    print(эртай) # алиби

# func()
# print(nastya)   - NameError: name 'nastya' is not defined

# example
count = 0

def add():
    print(count)
    count += 1 # UnboundLocalError: local variable 'count' referenced before assignment

def add():
    global count # доступ на изменение глобальной переменной count
    count += 1
    print(count)

add()
add()
add()
print(count)
# 1 2 3 3

# example
a = 'global'

def outer_func():
    a = 'enclosed'

    def inner_func():
        a = 'local'
        print(a) # local
    
    print(a) # enclosed
    inner_func()

print(a) # global
outer_func()

# global enclosed local


# example
def count(i):
    counter = 0
    
    def add():
        nonlocal counter # доступ на чтение и изменение локальной переменной counter 
        print(counter)
        counter += 1
    
    for _ in range(i):
        add()

count(10)
# 0 1 2 3 4 5 6 7 8 9


# example
def func():
    a = '1'
    def inner_func():
        def inner2_func():
            nonlocal a # доступ на чтение и изменение локальной переменной a
            a = 2
        inner2_func()
    inner_func()
    print(a)
func() # 2


"=================================== Content from Platform ===================================="
# example
name1 = 'makers'                        # global scope
name2 = 'bootcamp'

def func9():
    name3 = 'helloworld'        # enclosing scope

    def func10():
        name4 = 'namespace'     # local scope

"=================================== LEGB ===================================="
# Built-in   [встроенная область]
# Global scope
# Enclosed scope   [замкнутая область]
# Local scope

# example
this_var_is_visible = 'You can see me inside and outside the function.'

def var_visibility():
    this_var_is_not_visible = 'You can see me only inside the function.'
    print(this_var_is_not_visible)
print(this_var_is_visible)
var_visibility()
# You can see me inside and outside the function.
# You can see me only inside the function.
# print(this_var_is_not_visible)   # NameError: name 'this_var_is_not_visible' is not defined. Did you mean: 'this_var_is_visible'?


# example
word = 'I am global'

def func_a():
    word = 'I am local'
    print(word)
func_a()
# I am local


# example enclosed scope
word0 = 'I am global'

def outer():
    word0 = 'I am enclosed'
    print(word0)

    def inner():
        word0 = 'I am local'
        print(word0)
    inner()
outer()
print(word0)
# I am local
# I am enclosed
# I am local
# I am global


# globals()  ---> prints dictionary in a global scope, возвращает текущий словарь глобального пространства имен
name = 'Makers'
name2 = 'Bootcamp'
print(globals())
# {'name': 'Makers'}


# locals() --> отображает словарь локального пространства имен
def func_(company):  # параметры функции являются локальными переменными
    name = 'Bootcamp'
    print(locals())

func_(company='Makers')
# {'company': 'Makers', 'name': 'Bootcamp'}


# example
def infor(name, age):
    name = 'Alice'
    age = 30 
    print(locals())

infor(name='Carly', age=34)
# {'name': 'Alice', 'age': 30}  --> именнованный аргумент отображается первее чем локальный аргумент


# изменение переменных вне области их функции
x = 20 
def func0():
    x = 40
    print(x)
func0()    # 40 
print(x)   # 20 


# example
my_list_ = ['makers', 'bootcamp', 'scope']
def func8():
    my_list_[-1] = 'namespace'
func8()


# example
x = 20
def func5(): 
    global x  # ключевое слово, которое перезаписывает значение x в глобальном пространстве
    x = 40
    print(x)
func5()    # 40
print(x)   # 40


# example [nonlocal]
def outer_():     # enclosed scope
    name = 'makers'

    def inner():  # local scope
        nonlocal name  # для обращения к переменной, которая находится в замкнутом пространстве имен - nonlocal будет искать переменную на замкнутом пространстве (в замкнутой области видимости)
        name = 'bootcamp'

    inner()    # enclosed scope
    print(name)
outer()   # makers