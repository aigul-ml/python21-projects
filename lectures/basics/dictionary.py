"======================== Dictionaries =================================="

# словарь - изменяемый, итерируемый, неиндексируемый и неупорядоченный тип данных, в котором значения хранятся в парах (ключ: значение)

import numbers
from operator import contains


dict = {'a': 'Hello', 'b': 2, 'c': 3}
print(dict['a'])    # Hello

# ключами в словаре могут являться все неизменяемые типы данных 
# значениями в словаре могут являться любые типы данных 
# ключи должны быть уникальными т.е. не повторяться 

dict_ = {
    1: 'hello',
    'a': 4,
    4.5: {'a': 5},      # to print value 5 --> print(dict_[4.5]['a'])
    # {'s': 5}: 44   --> TypeError 
}


"============================= создание словарей ========================================"

dict1 = {'a': 9}
dict2 = dict( [ ('key1', 'value1'), ('key2', 'value2')] ) 
# dict2 = {'key1': 'value1', 'key2': 'value2'} 

dict5 = dict('ab')     # ValueError 

dict5 = dict(['ab'])   # {'a': 'b'} 

dict5 = dict(['abc'])  # Error because we have included more than 2 values and it cannot create a pair for key: value in dict

a, b = 5, 4
a, b = b, a 

a, b = 1, 2, 3      # Error because we have more values for keys 

dict4 = dict(['ab', 'cd', 'de'])  
# {'a': 'b', 'c': 'd', 'd': 'e'}

key1, value1 = 'ab'
dict5[key1] = value1     # {'a': 'b'}

"============================== Методы словаря ====================================="
dict_.clear()     # clears dictionary
print(dict_)     # {} prints empty dictionary 

dict_ = dict_.fromkeys([1, 2, 4])
print(dict_)      # {1: None, 2: None, 4: None}

dict_ = dict.fromkeys([1, 2, 4], 'hello')
print(dict_)      # {1: 'hello', 2: 'hello', 4: 'hello'}

dict_ = {'a': 2, 'a': 3, 'a': 4}
print(dict_)      # {'a': 4}

dict_['a'] = 5
print(dict_)      # {'a': 5}

dict_ = {'a': 1, 'b': 2}
dict_['a']      # 1 
dict_['c']      # KeyError

# get method used to get value of requested key 
dict_.get('a')     # 1 
dict_.get('c')     # None

dict_.get('c', 5)   # 5
dict_.get('a', 5)   # 1 

# keys 
dict_.keys()    # returns keys from values 

dict_.values()   # returns values from keys 

dict_.items()   # dict_items([('a', 1) ('b', 2)])

# 
for i in range(1, 11):
    print(i)


dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {3: 'd', 4: 'e'}
dict1.update(dict2)
# update method добавляет пары из второго словаря в первый 
print(dict1)       # {'a': 5}

# pop method удаляет пары по ключу и возвращает значение 
print(dict1.pop(3))    # d 
print(dict1)         # {1: 'a', 2: 'b', 4: 'e'}

# popitem method удаляет последнюю пару и возвращает пару 
print(dict1.popitem())

# LIFO last in first out ---> pop.items() uses this method 
# FIFO first in first out 

dict4 = {1: 'a'}
dict4[2] = 'b'
dict4[3] = 'c'
dict4[2] = 'a'
print(dict4.popitem())       # 



# ######################################################################## platform notes 

dict_ = {}
# print(type(dict_))    

dict_1 = dict()
print(type(dict_1))


my_dict = {
    "name": 'Sam', 
    "lastname": 'White',
    "age": 23
}
print(type(my_dict))


ny_dict = dict(a=1, b=2, c=3)    # именнованный аргумент ключ=значение ---> key: value 
print(my_dict)

my_dict2 = {'a': 1, 'b': 2, 'c': 3}
print(my_dict2)

my_list = [['m', 1], ['a', 2], ['k', 3]]
my_dict = dict(my_list)   # {'m': 1, 'a': 2, 'k': 3}

# Methods 
#  get(key, None)

my_dict = {1: 'Tom', 2: 'John'}
my_dict.get(2)      # John


# clear 
my_dict.clear()    # deletes dictionay 


# copy 
my_dict.copy()   # copies dictionary 

# pop(key, default)   # deletes key: value and prints out deleted value 
dict__ = {'name': 'Kate', 'height': 170}
dict__.pop('height')

# popitem() deletes key: value
dict.popitem()
# deletes last key: value and prints out dictionary of deleted key: value 

# setdefault(key, default)

dict_new = dict(a=1, b=2, c=4)
print(dict_new.setdefault('b'))    # in case there is no requested key setdefault sets out requested default key

# update method 
# update()   объединяет - расширяет словари 
dict3 = {1: 'Tom', 2: 'Alice'}
dict4 = {4: 'John', 6: 'Ann'}
dict1.update(dict2)
print(dict1)
# {1: 'Tom', 2: 'Alice', 4: 'John', 6: 'Ann'}


# fromkeys(seq, value) method creates dictionary from sequences 
numbers = [1, 2, 3, 4, 5]
new_dict = dict.fromkeys(numbers, 'Makers')
print(new_dict)
# {1: 'Makers', 2: 'Makers', 3: 'Makers', 4: 'Makers', 5: 'Makers'}


# example 2
numbers = list('makers')
new_dict = dict.fromkeys(numbers, 'Makers')
print(new_dict)
# {'m': 'Makers', 'a': 'Makers', 'k': 'Makers', 'e': 'Makers', 'r': 'Makers', 's': 'Makers'}

# перебор элементов словаря 
# for    items()    keys()      values()

slovar = {'name': 'Kate', 'height': 173, 'weight': 60}
print(slovar.items())
# ([('name': 'Kate', 'height': 173, 'weight': 60)])     returns list with sets of key: value


print(slovar.keys())
# prints out only keys 
# slovar_keys(['name', 'height', 'wewight'])       list with only key elements
fruit = {
    'banana': 1, 
    'apple': 3,
    'avocado': 5
}

for key, value in fruit.items():
    if value == 2:
        print(key)



print(slovar.values())
# prints only values 

contacts = {
    'Alice': '0703933732',
    'John': '0997343434'
}

for info in contacts:
    print(info)     #  prints out only keys 

for name, tel in contacts.items():
    print(f'Name: {name}, tel: {tel}')     #  prints out key: values method items() prints out keys and values 

# вложенные словари - как они работают 
nested_dict = {
    'makers': {
        'alid': 23,
        'aisha': 27,
        'aidai': 21
    }
}

nested_dict['makers']    # prints out dictionary key: values 

print(nested_dict['makers']['aidai'])   # prints out value of 'aidai' key 
