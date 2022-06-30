# ######################################## June 21, 2022. Tuesday. Week 3/ 
# # ############################# Functions ############################# 
# именнованный блок кода (у него есть название), который может принимать аргументы и возвращать результат

from calendar import c
from distutils.log import info
from fnmatch import translate
from itertools import count
from turtle import right


def my_sum(a,b):
    return a + b
    
res = my_sum(5, 4)
print(res)
# print(a)  # will give NameError ---> will not print anything


"=============================== Параметры ================================================"
# параметры - локальные переменные внутри функции, значения которым мы задаем при вызове функции (переменные, которые мы указали внутри скобочек при создании функции (когда написали def)
# сначала определяем обязательные, потом с дефолтом, потом *, и в конце * *

"============================== Виды параметров ==========================================="
# 1. Обязательные: 

# 2. Необязательные: 

# 2.1 По умолчанию: со значением по умолчанию: объявляем переменную со значением через равно ---> def my_sum(a, b = 10)

# 2.2 args 

# 2.3 kwargs 

"================================ Aргументы ============================================="
#  аргументы - значения, которые мы передаем параметрам при вызове функции
#  сначала всегда передаются позиционные потом именнованные

"================================ Виды аргументов ============================================="
# 1. позиционные  
# 2. именнованные (ключ = значение)

# example 
def sum_or_add10(a, b = 10):     # b is parameter with default argument 10
    return a + b
print(sum_or_add10(2, 3))      # 5 
print(sum_or_add10(5))         # 15
print(sum_or_add10(2, 9))      # 11
print(sum_or_add10(15))        # 25

# example
def func(*args, **kwargs):

    # args - returns tuples: tuple, в который нам приходят все аргументы, которые были переданы через запятую (кроме обязательных и по дефолту)

    # kwargs - returns dictionary, в который нам приходят все аргументы, которые были переданы в виде ключ равно значение (кроме именнованных)

    print('args -', kwargs)
    print('kwargs -', kwargs)

func(1, 2, 3, 4, 5, 6, 7,)                             # (1, 2, 3, 4, 5, 6, 7) {}
func(1, 2, 3, 4, 5, 6, 7, {'a': 5})                    # (1, 2, 3, 4, 5, 6, 7, {'a': 5}) {}
func(1, 2, 3, 4, 5, 6, 7, {'a': 5}, a = 3, b = 5)      # (1, 2, 3, 4, 5, 6, 7, {'a': 5}) {'a': 3, 'b': 5}

# example
def func2(a, b = 5, *c, **d):
    print('a - a', a)           # a - a 10
    print('b - b', b)           # b - b 5
    print('c - c', c)           # c - c ()
    print('d - d', d)           # d - d {}
     
# func2()   - TypeErrpr: func2() missing 1 required positional argument: 'a'
func2(10)
# func2(10, 20, 30, 40, a = 5, b = 6)           # TypeError 
func2(10, 20, 30, 40, c = 5, d = 6)             # d - d {'c': 5, 'd': 6}


# example
def aigerim():
    marker = nastya()
    print("Nastya brought marker", marker)

def nastya():
    print("bring marker")
    return "blue marker"

aigerim()

# example
def func():
    print(5)
    func()
# func()
# бесконечное количество 5 

# example
def my_len(obj):
    count = 0
    for i in obj:
        count += 1
    return count
print(my_len([1, 2, 3, 4, 5]))                 # 5 
print(my_len('absdfdsfsfsfs'))                 # 15

# example
database = {
    "Bekzat": "skala",
    "Ertai": "parol",
    "Aigul": "outtalent",
    "Oomat": "kyrgyzstan",
    "Imran": "12345",
    "Jiide": "return",
    "Manas": "make",
    "Arafat": "54321",
    "Eljaz": "parol",
    "Gulsana": "312", 
    "Erkayim": "aidin",
    "Beknaz": "arol", 
    "Edil": "kgfd",
    "Begayim": "makers",
    "Myrzayim": "bootcamp",
    "Zakir": "debug",
    "Daniel": "console",
    "Jibek": "1404", 
    "Aigerim": "moon02",
    "Kalys": "stol",
    "Yrys": "shuu",
    "Aiganysh": "qwerty",
    "Argen": "11172322",
    "Nurmuhammed": "nevernaiia",
    "Bektur": "0101",
    "Alan": "dushu pitona",
    "Jaanger": "oh blin",
    "Bohdan": "bohdan",
    "Aigerim": "blue marker",
    "Nastya": "python21"
}

def login(**data):
    username = data.get("username")
    password = data.get("password")

    if username in database:
        if password == database[username]:
            print("Success")
        else:
            print("Incorrect password")
    else:
        print("Incorrect username")

login(username = "Aigul", password = "mai")


# another version of above example 
def login(username):
    for i in range(3):
        if username in database:
            password = input("Enter password: ")
            if password == database[username]:
                print("Success")
                break
            else:
                print("Incorrect password")
        else: 
            print("Incorrect username")
            break

# example translator similar to Google 
def translate(string):
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"
    if string[0]in eng:
        dictionary = str.maketrans(eng, ru)
    else:
        dictionary = str.maketrans(ru, eng)
    return string.translate(dictionary)

print(translate(input("Enter word: ")))

"====================================== * ===================================================="
# * - знак умножения
# * - распаковка 
list_ = [1, 2, 3, 4, 5]
list2 = [*list_]                # * - распаковывает значения в списке в новый список 
print(list2, list_)             # [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]    


# example
dict_ = {'a': 3, 'b': 6}
dict2 = {**dict_}               # для распаковки словарей используются две * ---> **
print(dict2)                    # {'a': 3, 'b': 6}

"=================================== Content from Platform ===================================="
# example 
def subtract():
    num1 = 20
    num2 = 5
    print(num1 + num2)
    return num1 - num2
print(subtract())                    # 15


# example
def subtract1():
    num1 = 20
    num2 = 5
    print(num1 + num2)
    return num1 - num2

def function():
    print("I am calling subtract function.")
    variable = subtract1()
    return variable

print(function())
# I am calling subtract function.
# 25
# 15


# example
def welcome(name, last_name):
    return f'Welcome, {name} {last_name}'

name = input()
last_name = input()

print(welcome(name, last_name))


# example
def get_word(word):
    list_letters = list(word)
    return list_letters

def get_vowels(letters):
    vowels = ['a', 'o', 'y', 'i', 'e', 'u']
    list_vowels = [letter for letter in letters if letter in vowels]
    result = ''.join(list_vowels)
    return result

my_word = input('Please enter word: ')
print(get_vowels(get_word(my_word)))


# example
def info(name = 'Sam', age = 19):
    return f'{name} is {age} years old.'
print(info('John', age = 35))
# {'name': 'John', 'age': 89}


# example
def test_func(n1, n2 = 9):
    return n1 + n2
print(test_func(n1 = 10))
# 19 ---> n1 = 10 and n2 = 9 by default


# example
def create_profile(name, age, image = 'default.jpg'):
    return name, age, image
print(create_profile(name = 'Agu', age = 45, image = 'flower.png'))
# ('Agu', 45, 'flower.png')


# example
def func(required, *args, **kwargs):
    print(required)

    if args: 
        print(args)
    
    if kwargs:
        print(kwargs)

func('Makers', 'Bootcamp', 'Python', name = 'John', age = 89)
# Makers
# ('Bootcamp', 'Python')
# {'name': 'John', 'age': 89}


# example
def many(*args, **kwargs):
    print(args)
    print(kwargs)

many(1, 2, 3, name = 'Aigul', job = 'engineer')
# (1, 2, 3)   ---> tuple/ кортеж
# {'name': 'Aigul', 'job': 'engineer'}