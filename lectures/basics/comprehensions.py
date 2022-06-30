"===================== comprehensions ==============================="
# comprehensions - генерация последовательностей в одну сторону, используя цикл 
# 1. результат for элемент in итерируемый объект
# 2. результат for элемент in итерируемый объект if фильтр

"============== List comprehension ================"
# создать список состоящий из чисел
import imp
from unittest import result


list = []
for i in range(1, 10):
    list.append(i)
#  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

list1 = list( (i for i in range(1, 10)) )
#  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

list2 = [i for i in range(1, 10)]
#  list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

# создать список, состоящий из четных чисел
list0 = []
for i in range(1,10):
    # if not 0 
    if not i % 2:
        list0.append(i)
# comprehensions 
list0 = [i for i in range(1, 10) if not i % 2]

list0 = [i for i in range(2, 10, 2)]    # we begin from 2 and include steps 

# list0 = [2, 4, 6, 8]

list0 = [print(i) for i in range(10)]    
# [None, None, None, None, None, None] 

# 
print([input() for i in range(10)])
# на каждой итерации запрашивает инпут 


# создать список, состоящий из чисел от 1 до 10 но вместо чисел написать 'четное' или 'нечетное'
          # тернарный оператор - 2 варианта результата
list3 = [ (i, 'нечетное' if i % 2 else 'четное') for i in range(1, 10) ]
print(list3)

# создать список из чисел list4 заменив их на четное или нечетное
list4 = [1, 'hello', 2.0, 34.0, 'print', 3434]

list4 = [ 'нечетное' if i % 2 else 'четное' 
    for i in list4 
    if type(i) == int or type(i) == float]

print(list4)
# ['нечетное', 'четное', 'четное', 'четное']

"============= Dict comprehension =================="
'создать словарь, где ключи - числа от 1 до 10, а значения эти числа ввиде строки'
dict_ = dict( (i, str(i)) for i in range(1,11) )
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

# 'даны 2 списка, создайте словарь, где ключи - элементы 1 списка, а значения - второго'
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

dict_ = dict( (list1[index], list2[index]) for index in range(len(list1))  )
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

dict_ = { list1[index]: list2[index] for index in range(len(list1)) }
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# создайте копию словаря 
dict8 = {"a": 1, "b": 2, 4: "c"}
dict6 = { key: value for key, value in dict8.items() }
# dict8 = {"a": 1, "b": 2, 4: "c"}

# меняем ключи значения местами в новом словаре 
dict8 = {"a": 1, "b": 2, 4: "c"}
dict5 = { value: key for key, value in dict8.items()}
# {1: 'a', 2: 'b', 'c': 4}

# имеется словарь, где значения - список с числами - создайте новый словарь, где значения - сумма тех чисел 
dict0 = {
    'a': [1, 2, 3, 4, 5],
    'b': [1, 5, 7, 89, 90],
    'c': [45, 23, 43, 56, 87],
    'd': [56, 34, 12, 45, 45]
}

dict1 = { key: sum(value) for key, value in dict0.items() }
# {'a': 15, 'b': 34, 'c': 149, 'd': 134}

"=============== вложенные comprehensions ============================="
# создайте словарь где ключами будут числа от 1 до 10 а значениями будут списки от 1 до числа, который является ключом
# 
dict0 = { i: list(range(1, i +1)) for i in range(1, 6) } 
print(dict0)
# { 1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5] }

dict0 = { i: [j for j in range(1, i+1)] for i in range(1, 6) }
print(dict0)


# создать список, состоящий из 10 списков, в которых строка 'hello world' повторяется 5 раз 
list0 = [
    ['hello world' for i in range(5)]
    for i in range(10)
]

# создайте список, состоящий из 10 списков, в которых строка "hello world" повторяется 5 раз
list_ = [
    [i for i in range(5)]
    for i in range(10)
]
# [[0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4]]


# ###############################################################
# comprehensions - content from platform 
# ###############################################################
# for 
list_ = []
for num in range(1, 21):
    list_.append(num  * 2)    # добавляет элемент в конец списка
print(list_)

# list comprehension
list_ = [num * 2 for num in range(1, 21)]
print(list_)

# list comprehension example 
list_users = ['Alice', 'Sam', 'Sandy', 'Ben', 'John']
invitations = ['You are invitied ' + name for name in list_users]
print(invitations)
# ['You are invited Alice', 'You are invited Sam', 'You are invited Sandy', 'You are invited Ben', 'You are invited John']


# if in list comprehensions - положительные числа которые делятся на 2 без остатка 
list1 = [10, 5, 4, 3, 2, 0, 9, 14]
list2 = [num for num in list1 if num % 2 == 0 and num > 0]
print(list2)
# [10, 4, 2, 14]

# отфильтровать строки, в которых содержатся только цифры 
strings = ['1994', '1995', '1994 year', '2020']
list_ = [ year for year in strings if year.isdigit() ]
print(list_)
# ['1994', '1995', '2020']


# создать список длины строк из первого списка 
list_ = ['Rachel', 'John', 'Alice', 'Sam']
# переопределяем нашу строку
list_ = [len(name) for name in list_]
# [7, 4, 5]

# ветвление в list comprehensions 
list_ = [4, -5, 56, 89, 0, 2, 8, 4, 5, 7]
list_ = [ x if x < 0 else x ** 2 for x in list_ ]
print(list_)

# 
list_ = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
#                                               фильтр чисел, которые делятся на 2 без остатка
list_ = [x if x < 0 else X ** 2 for x in list_ if x % 2 == 0]
print(list_)
# [-12, 0, 4, 64, 16]


# посчитать количество символов в строке, а эти строки хранятся у нас в списках
names = ['raychel', 'john', 'peter', 'jessica', 'bill', 'steven', 'steven123', 'sandy2345', 'james']

filtered_names = [
    x + 'MAKERS' 
    if len(x) >= 5 
    else x + 'makers' 
    for x in names 
    if x.isalpha()]
print(filtered_names)
# [ 'raychelMAKERS', 'johnmakers', 'peterMAKERS', 'jessicaMAKERS', 'billmakers', 'stevenMAKERS', 'jamesMAKERS']


# используем традиционный цикл for 
names = ['raychel', 'john', 'peter', 'jessica', 'bill', 'steven', 'steven123', 'sandy2345', 'james']
filtered_names = []
for x in names:
    if x.isalpha():
        if len(x) >= 5:
            result = x + 'MAKERS'
            filtered_names.append(result)
        else:
            result = x + 'makers'
            filtered_names.append(result)
print(filtered_names)


# каждый list comprehension можно переписать в цикл for
# но не каждый цикл for можно выдать в лист comprehensions

# сделать статистику пользователей 
john = { 'name': 'John', 'age': 22 }
raychel = { 'name': 'Raychel', 'age': 23}
peter = {'name': 'Peter', 'age': 17}

users = [john, raychel, peter]
ages = [users.get(('age', None) for user in users)]
print(ages)
# [22, 23, 17]

bigger = 0
smaller = 0 
count = 0 

for age in ages:
    if age >= 18:
        bigger +=1 
    else:
        smaller += 1
    count += 1

# formula to count percentage
bigger = bigger * (100/ count)
smaller = smaller * (100/ count)
print(f'процент пользователей с возврастом больше 18: {round(bigger)} процента')
print(f'процент пользователей с возврастом меньше 18: {round(smaller)} процента')
# процент пользователей с возврастом больше 18: 67 процента
# процент пользователей с возврастом меньше 18: 33 процента

# matrices вложенный list comprehension
# трехмерная матрица
matrix = [
    [0, 2, 5, 6],
    [7, 3, 0, 7],
    [5, 7, 1, 6]
]

# распаковываем нашу матрицу
uncompress = [n for row in matrix for n in row]
print(uncompress)
# выходит список распакованной матрицы [0, 2, 5, 6, 7, 3, 0, 7, 5, 7, 1, 6]

# используем цикл для этого же примера
uncompress = []
for row in matrix:
    for n in row:
        uncompress.append(n)
    print(uncompress)
    # [0, 2, 5, 6, 7, 3, 0, 7, 5, 7, 1, 6]


# example
# создать список от 0 до 100тыс используя цикл а потом вариант использования list comprehension
# и проверим сколько времени потребовалось для создания данного списка
from datetime import datetime

start = datetime.now()
# показывает текущее время - засекаем начало создания списка
list_ = []
for i in range(100000):
    list_.append(i)
print(datetime.now() - start)
# 0:00:00.011179

# создание такого же списка, но используя list comprehension
list_ = [i for i in range(100000)]
print(datetime.now() - start)
# 0:00:00.004236  - ушло намного времени чем когда мы использовали циклы 

# #####################################################################
# dictionary comprehensions 
dict_abc = {'a': 1, 'b': 2, 'c': 3}
dict_123 = {key: value for key, value in dict_abc.items()}
print(dict_123)
# {'a': 1, 'b': 2, 'c': 3}

dict_123 = {value: key for key, value in dict_abc.items()}
print(dict_123)
# {1: 'a', 2: 'b', 3: 'c'}

# умножить значение ключей на 2
dict_abc = {'a': 1, 'b': 2, 'c': 3}
dict_123 = {key: value * 2 for key, value in dict_abc.items()}
print(dict_123)
# {'a': 2, 'b': 4, 'c': 6}

# сделать значение ключей - буквы заглавные 
dict_abc = {'a': 1, 'b': 2, 'c': 3}
dict_123 = {key.upper(): value for key, value in dict_abc.items()}
print(dict_123)
# {'A': 1, 'B': 2, 'C': 3}

# использование условий в dict comprehensions 
dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': -4, 'e': -7}
new_dict = {key.upper(): value ** 3 for key, value in dict_abc.items() if value > 0}
print(new_dict)
# {'A': 1, 'B': 8, 'C': 27}


# создаем вложенные словари 
a = {
    'fruits': 
    {'apple': 100, 'orange': 60},
    'vegetables':
    {'cucumber': 28, 'tomato': 63}
}

# овощи и фрукты подорожали т.е. к каждому значению мы должны добавить 3 
b = {key: {inner_k: inner_v + 3 for inner_k, inner_v in value.items()} for key, value in a.items()}
print(b)
# {'fruits': {'apple': 103, 'orange': 63}, 'vegetables': {'cucumber': 31, 'tomato': 66}}

# ######################################################################
# set comprehensions 
# example 1 
list_ = [-2, 4, -5, 3, 8, -2, 3, 7]
# создадим множество 
# множество - это коллекция, которая содержит только уникальные элементы т.е. множество не будет содержать повторяющиеся элементы 
set_ = {num for num in list_}
print(set_)
# {3, 4, 7, 8, -5, -2}   

# умножим каждое число на 2 и фильтруем только положительные числа 
set_ = {num * 2 for num in list_ if num > 0}
print(set_)
# {6, 8, 14, 16}  


# 
dict_ = {'a': 1, 'b': 2, 'c':3}

# возвести все значения словаря во вторую степень 
new = {value ** 2 for value in dict_.values()}
print(new)
# {1, 4, 9} - множество 