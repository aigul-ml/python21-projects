"====================  Строки  =================="
# строки - тип данных, который предназначен для хранения текста (последовательности символов)б заклеченного в одинарные или двойные кавычки

# строки - это неизменяемый тип данных 

# Синтаксис: 

string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error = 'неправильная строка"
string3 = "don't"  # внутри двойных кавычек все одинарные - просто символы 
string4 = ' "Makers bootcamp" '  # внутри одинарных кавычек все двойные - просто символы 
# print(string3, string4) 

string5 = ''' 
Многострочный текст 
в одинарных кавычках

Тут можно ставить "любые" 'кавычки'
""""

'''

string6 = """
Многострочный текст 
в двойных кавычках

Тут можно ставить "любые" 'кавычки'
''''''
"""

"=====================  Экранизация строк  ==================================="
# Экранизация спец - символов 
'\n' # перенос на новую строку 
'hello \n world' 
# hello 
# world

'\t' # табуляция 
'hello \t world' 
# hello      world

'\\' # отображение \ (потому что он является инструкцией, которая влияет на наш код)

'\'' # отображение кавычки ' 

"\"" # отображение кавычки "

'\r' # возвращение каретки в начало строки
'My website is Latracal \rSolution'
# Solutionte is Latracal

'\v' # перенос на новую строку с смещением вправо на длину предыдущей строки


"============================  Форматирование строк  =========================================="
title = 'sushi'
price = 1500
format1 = f'Название: {title}, Цена: {price}'
# Название: sushi, Цена: 1500


format2 = 'Название: %s, Цена: %s'
print(format2 % ("суши", "250"))
print(format2 % ("суши", "250"), format2 % ("суши", "250"), sep = '\n')


format3 = 'Название: {}, Цена: {}'
print(format3.format('Шакарап', '35'))

"====================== Методы строк ============================"
# методы типо данных - функции, к которым мы обращаемся через точку
dir(str)   # to see all the methods that belong to strings - позволяет посмотреть все методы класса 

'HELLO'.lower()   # returns 'hello'
'hello'.upper()   # returns 'HELLO' 
'Hello'.swapcase()     # returns 'hELLO'  - changes lower cases into upper case and vice versa
'hello'.title()     # 'Hello'  - formats into title format - titlecases
'hello world'.capitalize    # 'Hello world'   - returns capitalized first word only 
'hello'.center(3)   #'        hello     '
'hello'.center(11, '-')    # '---hello---'
'hello'.count('l')    # 2 counts requested letters
'hello'.count('ll')   # 1 
'hello hello'.count('hello')     # 2 
'hello world'.startswith('hell')   # True - boolean condition 
'hello world'.endswith('ld')       # True 

'hello world'.find(' ')     # 5 returns its index 
'hello world'.find('o')     # 4 
'hello world'.find('wo')    # 6

'hello world'.split()       # ['hello', 'world']
'hello world'.split('o')    # ['hell', ' w', 'rld']

'$'.join(['hello', 'world'])    # 'hello$world'
' '.join(['hello', 'world'])    # 'hello world'
''.join(['hello', 'world'])     # 'helloworld


# конкатинация - склеивание строк 
'hello' + 'world'      # helloworld 
'hello' + ' ' + 'world'  # hello world 

 
"=================== Индексы ========================"
# индекс - порядковый номер символа в строке 
'hello world'
'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string9 = 'hello world'
string9[0]   # 'h'
string9[10]  # 'd'
string9[5]   # ' '

# срез - подстрока строки 
string9[0:5]     # 'hello'
string9[0:6]     # 'hello'
string9[2:4]     # 'll'
string9[0:5][2:4]  # 'll'

string9[:5]      # 'hello'
string9[6:]      # 'world'
string9[:]       # 'hello world' 
string9[0:11:2]  # 'hlowrd'
string9[::3]     # 'hlwl'
string9[::-1]    # 'dlrow olleh'
string9[::-2]    # 'drwolh'

# ================ Extra Information ==========================
a = 5 
b = 5
print(id(a))
print(id(b))

print(hash(a))
print(hash(b))

a = 'hello'
b = 'hello'
print(hash(a))

# id(a) = id(b)
# hash(a) = hash(b)


text1 = 'Makers'
text2 = 'Bootcamp'
print(text1, text2)