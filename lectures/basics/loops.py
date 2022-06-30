"=================== looos [циклы] ==========================="

# циклы - это блок кода, который повторяется несколько раз 

# while - до тех пор/ пока что - это цикл, который работает до тех пор пока условие верно 

# for - цикл, который работает с итерируемыми объектами. цикл заканчивает свою работу, когда он дошел до последнего элемента в итерируемом объекте 

# while True: 
    #print(5)    # will work infinitely because True has not changed 

from email.policy import strict


count = 10
while count !=0: 
    print(count)  
    count = count - 1    # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
print('end')

a = 0
while a:
    print('hello') # ne rabotaet потому что bool(a) False 


# for 
for i in [1, 2, 3]: 
    print(1)     # 1 2 3 

for i in range(1, 10):
    print(i)     # 1 2 3 4 5 6 7 8 9 

for i in '12345':
    print(i)    # '1' '2' '3' '4' '5'

# question
num = 12345678
sum = 0
for i in str(num):
    sum = sum + int(i)
print(sum)   # 36 

# 
string = 'hello'
string2 = 'world'

for i in range(len(string)):
    print(i, strict[i], string2[i])

# 0 h w 
# 1 e o 
# 2 l r 
# 3 l l
# 4 o d 


# 
list_ = [1, 2, 3]
for i in list_:
    print(i)
    list_.append(4)    # will print 4 infinite number


# 
string = 'hello'
for i in string:
    print(i)
    string = string + 'hello'
    print(string)
# отработает только 5 раз, потому что у переменной string ссылка  на 68 не менялась, а у цикла на строке 66 нет

# break - полностью выйти из цикла 
# continue - перейти к следующей итерации 

for i in range(10):
    if i == 3:
        break
    print(i)    # 0 1 2 

for i in range(10):
    print(i)
    if i == 3:
        break    # 0 1 2 3 

# continue 
for i in range(10):
    if i == 3:
        continue
    print()     # 0 1 2 4 5 6 7 8 9 


for i in range(10):
    print()     # 0 1 2 3 4 5 6 7 8 9 
    if i == 3:
        continue


for i in range(10):
    print()     # 0 1 2 3
    if i == 3:
        break

for i in range(10):
    if i == 3:
        break
    print()     # 0 1 2 

for i in range(10):
    if i < 3:
        break
    print()     # 3 4 5 6 7 8 9


for i in range(10):
    print()     
    for j in range(10):
        print(j)
        if j == 5:
            break
        if i == 2:
            break
        # 0
        # 0 1 2 3 4 5 
        # 1 
        # 0 1 2 3 4 5 

# remove all items 
list3 = [2, 3, 4, 5, 6, 2, 5, 3, 5, 6, 2, 3, 2]
while 2 in list3:
    list3.remove(2)
print(list3)

"==================== итерирование словарей ======================================"
dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# при итерации словаря мы будем получать его ключи 
for key in dict4:
    print(key)
    # 'a' 'b' 'c' 'd'

# при итерации dict4.keys()  - мы получим его ключи 
for key in dict4.keys():
    print(key)

# при итерации dict4.values(), мы будем получать значение словаря
for value in dict4.values():
    print(value)

# выводим значения 
for key in dict4:
    print(dict4[key])

# при итерации dict4.items() мы будем получать tuples из ключа и значения
for items in dict4.items():
    key = items[0]
    value = items[1]
    print(key, value)

# можем распаковать tuple на 2 переменных 
for key, value in dict4.items():
    print(key, value)

# for key, value in dict.keys()
# ValueError: not enough values to unpack (expected 2, got 1)
# потому что метод keys() возвращает нам только 1 элемент, а мы распаковываем его на 2 переменные 

for a, b, c in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
    print(a, b, c)
    # a = 1 b = 2 c =3 (iter 1)
    # a = 4 b = 5 c = 6 (iter 2)
    # a = 7 b = 8 c = 9 (iter 3)

# 
for i in []:
    print('for')
    if i == 2:
        break
else:  # сработает если цикл вообще ни разу не отработал или не был прерван break
    print('else')


# 
a = 1 
while a:
    print('while')
    a -= 1
else:
    print('else')
# while
# else 


# 
a = 1 
while a:
    print('while')
    if a == 1:
        break
else:
    print('else')
# while
