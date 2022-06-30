"================= Логические операторы =============================="
# логические операторы - выражения, которые возвращают True, если правда False - если ложь 
5 == 5  # True 
4 == 5  # False 

5 != 5  # False 
5 != 2  # True 

5 > 10  # False 
10 > 5  # True 
5 > 5   # False 
5 < 10  # True 
10 < 5  # False 
5 < 5   # False 

5 <= 10 # True 
10 <= 5 # False 
5 <= 5  # True 
10 >= 10 # True
10 >= 5  # False 

'5' == 5   # False 

"=================== Booleans ==============================="


# Booleans 
# булевый тип данных - имеет всего 2 значения - True/ False 
bool(1)   # True - потому что все числа выдают True 
bool(0)   # False 
bool(-277)  # True 

bool('hello world')     # True 
bool('')       # False 
bool(' ')      # True - если хоть один символ - True, пустое значение - False 
bool(False)    # False 
bool(True)     # True

"=================== and or ================================="
# and - и
# or - или
a == 5 and b == 6     # True 
a == 5 and b ==5      # False 
a == 5 or b == 5      # True 
a == 4 or b == 5      # False 

# если обе части выдают True то будет True
# если обе части выдают False  то будет False 
# 1. если одна часть True, вторая False  --> 
# 2. если одна часть False, вторая True   --> False

not True    # False 
not False   # True 


"==================== Non Type ========================================="

# None - тип данных с одним значением None, который используется для обозначения пустых значений или отсутствия значений

bool(None)     # False 
bool('None')   # True 


a = None 
print(bool(a))   # False 
print(a is None) # True 
#  is это проверка на полное соответствие 


"============================ Условные операторы ===================================="
# условные операторы нужны для того, чтобы при разных входных данных код работал соответственно

if условие:
    тело1 - логика1 

if условие1 - логика1:
    тело1

elif условие2:
    логика2

# в одной конструкции мы можем использовать неограниченное количество elif
# в одной конструкции мы можем использовать только один if
# else мы также можем использовать только один раз или не указывать вообще

a = int(input('Enter number: '))     # input always returns string data type 
print(a)
print(type(a))

if a > 0:
    print(f'Number {a} - positive')

elif a < 0: 
    print(f'Number {a} - negative')

else:
    print(f'Number {a} is 0')


"======================= FizzBuzz ================================"
# выведите число от 1 до 100
# если число равно 3 - вывестi Fizz
# если число кратно 5 - вывести Buzz
# если число кратно и 5 и 3 - вывести FizzBuzz
# если число не кратно ни 3 ни 5 - вывести число 

#  задачка на циклы 

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0: 
        print('FizzBuzz')
    elif i % 3 == 0: 
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# Another version of this task 
for i in range(1, 100):
    if i % 3 == 0: 
        if i % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i % 5 == 0: 
        print('Buzz')
    else:
        print(i)


"========================== Tertiary operators/ тернарные операторы ================================================"
# условия в одну строчку 
тело1 if условие else тело2

res = 'Hello' if a == 55 else 'Bye'
print(res)
# Hello если а == 5 
# Bye если а != 5 



