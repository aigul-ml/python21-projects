# example 1 
from functools import reduce


a = [1, 2, 3, 4]
b = []
numbers = ''

def func(a):
    for i in a: 
        if i > 1: 
            b.append(i)
    global numbers
    for i in b: 
        numbers += str(i)
func(a)
print(numbers)


# example with comprehensions 
d = {
    k: v for k, v in zip(range(10), range(10, 21))
}
print('d: ', d)
# d:  {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}


# example 
list_ = [1, 2, 3, 4, 5, 6, 7]

list2 = [i**2 if i >3 else i for i in list_ if i % 2 != 0]
print(list2)  # [1, 3, 25, 49]


# example
d2 = {
    None: 20
}
print(d2)
# {None: 20}


# example 

d4 = {
    k if k % 2 == 0 else None: v if v % 2 == 1 else v ** 2 for k, v in zip(range(10), range(10, 21)) if k % 2 == 0
}
print(d4)
# {0: 100, 2: 144, 4: 196, 6: 256, 8: 324}


# example
d3 = {}
for k, v in zip(range(10), range(10, 21)):
    if k % 2 == 0: 
        if v ==3:
            key = k if k % 2 == 0 else None
            value = v if v % 2 == 1 else v ** 2
            d3[key] = value
print(d3)


# example
# method 1 
list5 = ['Paul', 'George', 'Ringo', 'John']
def func(name1, name2):
    if len(name1) > len(name2):
        return name1
    else:
        return name2
res = reduce(func, list5)

# method 2
res1 = reduce(lambda name1, name2: name1 if len(name1) > len(name2) else name2, list5)

print(res)
print(res == res1)
# George
# True

# method 3
res3 = list5[0]
for i in list5:
    if len(i) > len(res3):
        res3 = i
print(res3)


# example
dict_ = {'a': 3, 'b': 4, 'c': 5}

dict2 = {k : v + 1 if v > 3 else v for k, v in dict_.items()}
print(dict2)


# example
res9 = list('hello')
res10 = []
for i in 'hello':
    res10.append(i)
print(res9)
print(res10)
# 'h', 'e', 'l', 'l', 'o']
# ['h', 'e', 'l', 'l', 'o']


# example
names = ['joHN', 'MAry', 'OleG', 'Name']
def rename(name):
    return name.title()

# method 1 
resk = []
for i in names:
    resk.append(rename(i))
print(resk)

#  method 2 
resd = map(rename, names)
rest = list(resd)
print(rest)
# ['John', 'Mary', 'Oleg', 'Name']
# ['John', 'Mary', 'Oleg', 'Name']

# method with lambda
res = list(map(lambda name: name.title(), names))
print(res)
# ['John', 'Mary', 'Oleg', 'Name']


# example with filter 
list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni']

def func(x):
    if len(x) > 7:
        return False
    return True

res = func(list_[0])
print(bool(res))   # True 


# example
dict_ = {'a': {'z': 1}, 'b': {'y': 2}, 'c': {'r': 3}}

dict2 = {k : inner_v 
for k, v in dict_.items() 
for inner_v in v.values()}

print(dict2)
# {'a': 1, 'b': 2, 'c': 3}


# global и nonlocal лезут немного выше
# Цифры в комментариях обозначают порядок срабатывания
numbers = '1'
def func(): # 1
    numbers = '2'
    def func2(): # 2
        nonlocal numbers
        numbers = '3'
        def func3(): # 3
            nonlocal numbers
            numbers = 1000
        func3() # 3
    func2() # 2
func() # 1


# Суть областей видимости в том, что можно использовать одинаковые названия в разных
# местах, и они не будут друг-другу мешать. В ООП это явление называют полиморфизмом.
class Person():

    def voice(self):
        print('hello')

class Lion:

    def voice(self):
        print('rar')

person = Person()
lion = Lion()
# Одинаковые названия, разный функционал, не мешают друг-другу
person.voice()
lion.voice()
# Примеры можно найти даже в обычном питоне
list.pop
dict.pop
set.pop

######################################################################

# Примеры одинаковой логики, в comprehension'ах, и через обычный цикл for

# comprehension
d = {
    # Тернарные операторы можно использовать даже тут
    k if k % 2 == 0 else None: v if v % 2 == 1 else v * 2
    for k, v in zip(range(10), range(10,21))
    # Эти if срабатывают первее всего
    if k % 2 == 0 if v > 15
}

# Цикл
d1 = {}
for k, v in zip(range(10), range(10, 21)):
    if k % 2 == 0:
        if v > 15:
            key = k if k % 2 == 0 else None
            value = v if v % 2 == 1 else v * 2
            d1[key] = value

# Результаты идентичны
print("➡ d :", d)
print("➡ d1 :", d1)
print(d == d1)


###################### ЗАДАНИЯ ######################
"""
Создайте переменную list_ и сохраните в нем список со строками. Найдите самое длинное имя из списка функцией reduce. Результат сохраните в новой переменной result и выведите в консоль.
"""
from functools import reduce

list_ = ['Paul', 'George', 'Ringo', 'John']

# способ 1 (пошагово)
def func(name1, name2):
    if len(name1) > len(name2):
        return name1
    else:
        return name2
res = reduce(func, list_)
print("➡ res :", res)

# способ 2 (одна строка)
res2 = reduce(lambda name1, name2: name1 if len(name1) > len(name2) else name2, list_)
print("➡ res2 :", res2)

# способ 3 (через цикл)
res3 = list_[0]
for i in list_:
    if len(i) > len(res3):
        res3 = i
print("➡ res3 :", res3)

# Вывод во всех случаях идентичен
print(res2 == res3)
print(res2 == res)

##################################
# Через for можно сделать вообще все
res1 = list('hello') # ['h', 'e', 'l', 'l', 'o']
res2 = []
for i in 'hello':
    res2.append(i)# ['h', 'e', 'l', 'l', 'o']
print(res1)
print(res2)

###################################

# Изменить имена тка, чтобы первая букыв была заглавной, остальные строчными
names = ['joHN', 'MAry', 'OleG', 'Name']

############## MAP ##################
# способ 1 (работа map под капотом)
def func(name):
    return name.title()
res = []
for i in names:
    res.append(
        func(i)
    )
print("➡ res :", res)

# способ 2 (по шагам)
import sys
# Map возвращает генератор
map_ = map(func, names)
# Map отдает по одному элементу за раз, 
# и поэтому весит немного
print(sys.getsizeof(map_)) # Размер генератора в байтах
res = list(map_)
print(sys.getsizeof(res)) # Размер списка в байтах
# Генераторы одноразовые
res1 = list(map_)
print("➡ res :", res) # Результат есть
print("➡ res1 :", res1) # Генератор отдал все раньше, пустой список

# способ 3 (одна строка)
res = list(map(lambda name: name.title(), names))
print("➡ res :", res)


########## FILTER #############
# Отфильтровать все слова, оставив только те, длина которых больще 7
list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 

# способ 1 (под капотом)
def func(x):
    return len(x) > 7
res = []
for i in list_:
    if func(i):
        res.append(i)
print("➡ res :", res)

# способ 2 (пошагово)
def func(x):
    return len(x) > 7

filter_ = filter(func, list_)
res = list(filter_)
print("➡ res :", res)

# способ 3 (одна строка)
res = list(filter(lambda x: len(x) > 7, list_))
print("➡ res :", res)

######################
# Получить все слова с первой заглавной буквами, и остальными строчными, при этом отфильтровать, оставив только те, длина которых больще 7
list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 

# способ 1 (под капотом)
def map_func(x: str) -> str:
    return x.title()

def filter_func(x: str) -> bool:
    return len(x) > 7

res = []
for i in list_:
    if filter_func(i):
        res.append(map_func(i))
print(res)

# способ 2 (пошагово)
def map_func(x: str) -> str:
    return x.title()

def filter_func(x: str) -> bool:
    return len(x) > 7
list_ = ['inheritance', 'polymorphism'] 

filter_data = filter(filter_func, list_)
map_ = map(map_func, filter_data)
res = list(map_)
print("➡ map_ :", res)

# способ 3 (в одну строку)
# Более понятный синтаксис
# res = list(
#     map(
#         lambda x: x.title(), 
#         filter(
#             lambda x: len(x) > 7,
#             list_
#         )
#     )
# )

# То же, что выше, но в одну строку
res = list(map(lambda x: x.title(), filter(lambda x: len(x) > 7, list_)))
print("➡ res :", res)

######### ALL || ANY ########

# All возвращает True если все значения True-подобные
def all_(list_): # Как она работает под капотом
    for i in list_:
        if not i:
            return False
    return True

list_ = [True, False, False]

print(all(list_), all_(list_),)
# Any возвращает True если хотя бы одно значение True-подобное
def any_(list_): # Как она работает под капотом
    for i in list_:
        if i:
            return True
    return False

print(any(list_), any_(list_))
######


"""
Дан вложенный словарь dict_ (словарь состоящий из других словарей) в котором ключом является имя студента, а значением словарь с его оценками по 3 предметам.

Распечатайте новый словарь, где вместо оценкок будет название предмета, по которому студент имеет высший балл. Нужно использовать comprehension.

{'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}
"""


dict_ = {
    'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
    'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
    'Nik': {'history': 84, 'math': 85, 'literature': 87}
}

# res = {k: k2 for k, v in dict_.items() for k2, v2 in v.items() if v2 == max(v.values())}
# # res = {}

# for k, v in dict_.items():
#     for k2, v2 in v.items():
#         if v2 == max(v.values()):
#             res.update({k: k2})

# print(res)


# res = {k: list({k2: v2 for k2, v2 in v.items() if v2 == max(v.values())})[0]  for k, v in dict_.items()}
# print(res)

"""
1) try-except
2) functions
3) scopes
4) built-in functions
"""
# a = []

# def func():
#     global a
#     a = 6

# func()
# print(a)

# def my_sum(a, b):
#     # print(a + b)
#     return a + b

# res = my_sum(2, 5)
# print(res)
# print(my_sum(2, 5))








# names = [
#     {'visit2': ["deli", "india"]},
#     {'visit3': ['vladimir','russia']},
#     {'visit9': ['kursk','russia']}
# ]
# geo_logs = [key    for i in names for key, val in i.items() if 'russia' in val]
# geo_logs.sort()
# print(geo_logs)

# try:
#     a = 5 + 'asdda'
#     print(a)
# except (ValueError, TypeError):
#     print('error')
# else:
#     print('else')
# finally:
#     print('finally')

# a = [1, 2, 3]
# a[8]

table = ''

for i in range(200):
        table += chr(i)
print(table)