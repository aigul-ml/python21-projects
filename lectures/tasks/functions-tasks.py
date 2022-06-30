# Задание 1
# Создайте функцию add, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
import imp
from unittest import result

def add(num1, num2):
    result = num1 + num2
    return result
print(add(-3, -7))


# Задание 2
# Создайте функцию get_string_length() которая будет принимать строку. Функция должна возвращать длину этой строки.
# Пример: print(get_string_length('hello')) 
# Вывод: 5
def get_string_length(string):
    return len(string)
print(get_string_length('hello'))


# Задание 3
# Создайте функцию: get_type() которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
# Пример: get_type(5, 's') 
# Вывод: <class 'int'> 
#        <class 'str'> 
def get_type(param1, param2):
    type_param1 = type(param1)
    print(type_param1)
    type_param2 = type(param2)
    print(type_param2)
    return type_param1, type_param2
print(get_type(5, 's'))
# <class 'int'>
# <class 'str'>
# (<class 'int'>, <class 'str'>)


# Задание 4
# Создайте функцию divide() которая должна принимать 2 числа и возвращать результат их деления.
# Пример: print(divide(5, 10)) 
# Вывод: 0.5 
def divide(num1, num2):
    return num1 / num2
print(divide(5, 10))


# Задание 5
# Создайте переменную dict_ в котором будет хранится словарь.
# Затем создайте функцию def dictionary()
# которая принимает этот словарь. Пройдитесь по dict_ циклом и распечатайте все его ключи внутри функции.
dict_ = {
    'sultan': '342',
    'apple': '22323', 
    'google': '150000'
}

def dictionary(dict_):
    for k, v in dict_.items():
        print(k)
dictionary(dict_)


# Задание 6
# Создайте переменную num = 6. Затем создайте функцию check() которая принимает переменную num в качестве аргумента check(num) и возвращает "It is odd number", если это число нечетное и "It is even number" если переданное число четное.
# Пример: print(check(num)) 
# Вывод: It is even number 
num = 6
def check(num):
    if num % 2 == 0: 
        return 'It is even number'
    else: 
        return 'It is odd number'
print(check(8))


# Задание 7
# Создайте функцию: is_palindrome() которая будет принимать строку и проверить является ли она палиндромом.
# Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.
# Функция должна возвращать True или False. Пробелы и регистр учитывать нужно.
# Пример: print(is_palindrome('довод')) 
# Вывод: True 
def is_palindrome(string):
    if string.lower() == string.lower()[::-1]:
        return True
    else:
        return False 
print(is_palindrome('довод'))


# Задание 8
# Создайте функцию max_num() которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вернуть максимальное значение.
# Пример: print(max_num(10, 12)) 
# Вывод: 12 
def max_num(num1, num2):
    return max(num1, num2)
print(max_num(10, 12))


# Задание 9
# Создайте функцию: multiply_list() которая принимает список чисел и возвращает их произведение.
# Пример: print(multiply_list([1, 2, 3, 4, 5, 6])) 
# Вывод: 720 
def multiply_list(my_list):
    r = 1
    for i in my_list:
        r = r * i
    return r
print(multiply_list([1, 2, 3, 4, 5, 6]))


# Задание 10
# Создайте функцию sum_digits() которая принимает целое число и возвращает сумму всех его цифр.
# Пример: print(sum_digits(105)) 
# Вывод: 6 
def sum_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum
print(sum_digits(105))


"================================ Classroom Tasks ============================================="
# 1) Напишите функцию get_info, которая запрашивает у пользователя имя и фамилию, последовательно. Далее внутри get_info вызовите другую функцию generate_password, которая будет генерировать пароль при помощи конкатенации имени и фамилии пользователя и рандомных 7 чисел (в промежутке от 0 до 9). В конце функция get_info возвращает пользователю сгенерированный пароль.

def generate_password(param1, param2):
    import random
    ramdom_list = random.sample(range(1, 10), k = 7)
    random_list = [str(i) for i in ramdom_list]
    password = param1 + param2 + ''.join(ramdom_list)
    return password

def get_info(name = input('Enter your name: '), surname = input('Enter your surname: ')):
    password = generate_password(param1 = name, param2 = surname)
    return password

print(get_info())
    

# 2) Напишите калькулятор на функциях. У вас должна быть основная функция get_data, которая запрашивает два числа, и действие (сложение, вычитание, умножение, деление). И в зависимости от выбранного действия get_data должна вызывать ту или иную функцию, в которой будет прописан алгоритм выполнения действий. В конце выдается результат через функцию result.

def add(a, b):
    return a + b

def substract(a, b): 
    return a - b 

def multiply(a, b): 
    return a * b 

def division(a, b): 
    return a / b 

def result(param):
    return param

def get_data(action):
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))

    dictionary = {'+': add(num1, num2), '-': substract(num1, num2), '*': multiply(num1, num2), '/': division(num1, num2)}
    
    some_result = dictionary[action]   # хранится результат какой-то из функций - умн., дел., сложение или вычитание 
    return result(some_result)

action = input('Select action from below: +, -, *, /:')
print(get_data(action))


# 3) Напишите функцию, которая будет принимать 2 обязательных параметра: вкус мороженого и размер. И также функция может принимать необязательные параметры, которые могут выступать в качестве топпинга к мороженому. Выдайте результат

def ice_cream(name, size, **kwargs):    # **kwargs - возвращает словарь именнованных аргументов
    print(f'Your{name} ice-cream {size} size')

    if kwargs:
        print('Your toppings: ' + '\n')
        for value in kwargs.values():
            print('\t' + value)

ice_cream(name = 'chocolate', size = 'medium', topping1 = 'nuts', topping2 = 'coconut')