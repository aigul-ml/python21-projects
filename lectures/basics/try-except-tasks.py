# Задание 1
# Опишите полный синтаксис конструкции try-except:
# try: 
#     number = int(input('Enter number between 1 and 10: '))
#     print(number)
# except ValueError:
#     print('Please enter number, not a string.')

# Задание 2
# Дан следующий код:  
# b = 10
#  c = 11
# print(a)
# Обработайте ошибку, которая может возникнуть.
# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print('There is no variable - a.')

# Задание 3
# Напишите программу которая будет получать два числа через input num1, num2, и делить одно на другое. Обработайте ошибку, которая возникнет в случае, если второе число окажется 0 и выведите сообщение.
# К примеру, таким сообщением: На ноль делить нельзя

# try: 
#     num1 = int(input('Enter nunmber 1: '))
#     num2 = int(input('Enter number 2: '))
#     result = num1 / num2 
# except ZeroDivisionError: 
#     print('На ноль делить нельзя')


# Задание 4
# Напишите программу, которая будет получать через input 2 числа num1, num2 и будет печатать их сумму.
# Обработайте ошибку, которая возникнет, если пользователь введёт что-то кроме числа и выведите сообщение, например: Введите число! 
# try: 
#     num1 = int(input())
#     num2 = int(input())
#     total = num1 + num2
#     print(total)
# except ValueError:
#     print('Введите число!')

# Задание 5
# Создайте словарь, к примеру: dict_ = {'key1': 'value1', 'key2': 'value2'} 
# Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если такого ключа нет, например таким выводом в терминал: Нет такого ключа!  

try:
    dict_ = {'key1': 'value1', 'key2': 'value2'} 
    for k in k, v in dict_.items():
        print(k)
except KeyError:
    print('Нет такого ключа!')