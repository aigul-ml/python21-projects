# Calculator 

# Калькулятор работает только при вводе целых чисел. т.к. остальные операции ограничены темами и методами, которые мы еще не прошли - по этой причине довольно примитивный калькулятор, который функционирует строго по инструкциям тз. Спасибо

from time import perf_counter
from turtle import st

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
operand = input('Выберите операцию из следующих + - * / % ** // ')

if operand == '+':
    x = num1 + num2
    print(x)

if operand == '-':
    x = num1 - num2
    print(x)

if operand == '*':
    x = num1 * num2
    print(x)

if operand == '/':
    x = num1 / num2
    print(x)

if operand == '%':
    x = num1 % num2
    print(x)

if operand == '**':
    x = num1 ** num2
    print(x)

if operand == '//':
    x = num1 // num2
    print(x)

elif operand not in '+, -, *, /, %, **, //, :': 
    print('Данной операции нет в системе.')

