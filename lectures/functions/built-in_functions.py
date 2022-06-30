
"========================= built-in functions ========================================"

"===================================== lambda ========================================"
"lambda" # анониимная функция
# lambda параметры: что функция возвращает
add = lambda a, b: a + b
print(add(5,4)) # 9

"======================================= map ========================================"
"map" # фунция, которая принимает первым аргументом функцию, вторым итерируемый обьект. map возвращает генератор, в котором все элементы - результат принимаемой функции, в которую мы передали элемент из последовательности

map_gen = map(int, ["1", "2", "3", "4"])
print(map_gen) # <map object>
print(list(map_gen))

# map(int, ["1", "2", "3", "4"])
# int("1") -> 1
# int("2") -> 2
# int("3") -> 3
# int("4") -> 4
# list( map(int, ["1", "2", "3", "4"]) ) -> [1, 2, 3, 4]

res = list( map(lambda a: a + 1, [1,2,3,4,5]) )
print(res) # [2,3,4,5,6]


# example
map_gen = map(int, ['1', '2', '3', '4', '5'])
print(map_gen)
print(list(map_gen))  # [1, 2, 3, 4, 5]


# example
res = list(map(lambda a: a + 1, [1, 2, 3, 4, 5]))
print(res)  # [2, 3, 4, 5, 6]


"========================= map на цикле for ========================================"
func = lambda a: a + 1
# def func(a):
 #  return a + 1 
res = []

for e in [1, 2, 3, 4, 5]:
    res.append(func(e))
print(res)  # [1, 2, 3, 4, 5]


"======================================== filter ========================================"
# это функция, которая возвращает генератор, принимает функцию и итерируемый объект. результат будет последовательность из элементов итерируемого объекта, которые прошли фильтр (проверку)

# example
list_ = ['Elin', 'Alice', 'Alina', 'Stanford', 'Google', 'Behavox', 'Linda']
def  starts_with_vowels(name):
    vowels = 'AEOIUY'
    if name[0].upper() in vowels:
        return True
    return False

res = list(filter(starts_with_vowels, list_))
# res = list(filter(lambda name: name.upper().starts_with_vowels(tuple(vowels)), list_))
print(res)  # ['Elin', 'Alice', 'Alina']

"========================= filter на цикле for ========================================"
def starts_with_vowels(name):
    vowels = 'AEOIUY'
    return name.upper().startswith(tuple(vowels))

list_ = ['Ulin', 'Ylice', 'Blina', 'Stanford', 'Google', 'Behavox', 'Linda']

res = []
for name in list_:
    if starts_with_vowels(name):
        res.append(name)
print(res)  # ['Ulin', 'Ylice']


"===================================== reduce ========================================"
# нужно импортировать из библиотеки functools. эта функция принимает функцию и итерируемый объект и возвращает 1 результат
from functools import reduce
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def multiply(a, b):
    return a * b
res = reduce(multiply, list_)
print(res)   # 362880


"========================= reduce на цикле for ========================================"
list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def mul(a, b):
    return a * b

res = list_[0]
for b in list_[1:]:
    res = mul(res, b)  # ????????
print(res)     # 362880


"================================= enumerate ========================================"
# функция, которая принимает последовательность. возвращает генератор, в котором каждый элемент - tuple, состоящийй из числа и элемента из последовательности
# нумерует элементы начиная с нуля

list_ = ['a', 'b', 'c', 'd']
for i in enumerate(list_):
    print(i)
# (0, 'a') (1, 'b') (2, 'c') (3, 'd') 

for index, elem in enumerate(list_):
    print('index - ', index, 'elem -', elem)
    # index -  0 elem - a
    # index -  1 elem - b
    # index -  2 elem - c
    # index -  3 elem - d

for i in enumerate(list_[1:]):
    print(i)
    # (0, 'b')
    # (1, 'c')
    # (2, 'd')

for i in enumerate(list_[1:], 10):
    # начинает нумерацию с 10 
    print(i)
    # 10, 'b')
    # (11, 'c')
    # (12, 'd')


"================================= zip ========================================"
# соединяет последовательности 
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]  список из tuple
print(dict(zip(list1, list2)))
# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}


"================================= LeetCode ========================================"
# Output: "Capitalize The Title"
# Explanation:
# Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.

# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:

# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.

# "First Letter of Each Word"
title = "First leTTeR of EACH Word"
def capitalizeTitle(title):
    return " ".join([word.lower() if len(word) < 3 else word.title() for word in title.split()])
print(capitalizeTitle("First leTTeR of EACH Word"))