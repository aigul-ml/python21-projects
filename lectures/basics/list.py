"============================ lists ================================="
# списки - изменяемые, индексируемый, упорядоченный, итерируемый (мы можем пройти и сделать перебор каждого элемента) тип данных предназначенный для хранения всех типов данных в определенном порядке. 

list1 = [1, 2, 3, 4, 'hello', [0, 1, 2, 3], {'a': 3}]

list1[1]     # 2 
list1[4]     # [0, 1, 2, 3]
list1[4][0]  # 0 
list1[4][0]  # h
list1[-1]['a'] # 3
str(list1[4][0])

"=================== создание списков ==========================================="
list1 = [1, 2]
list2 = list('hello')        # ['h', 'e', 'l', 'l', 'o']
''.join(list2)     # hello 


list90 = list(range(1, 11))     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


"=================== list methods ==========================================="
dir(list)

# append(element) добавляет элемент в конец списка 
list3 = []
list3.append(1)
print(list3)     # 1 

list3.append('hello')
print(list3)    #[1, 'hello']

list3.append([1, 2, 3, 4])
print(list3)    # [1, 2, 3, 4]

list3.append(1, 2, 3)     # TypeErro: append() takes exactly one argument (3 given)

# append example 
guests = []
list_length = int(input('Enter number of guests: '))

for i in range(list_length):
    guest = input('Enter guest name: ')
    guest.append(guest)
print(guest)

# clear - очищает список удаляет все элементы списка 
list3.clear()
print(list3)     # [] empty list 


# count(element) 
# counts requested element in our list 
list4 = [1, 2, 3, 4, 1, 1, 1]
list4.count(1)     # 4
list4.count(2)     # 1 

# len method counts number of elements in our list 
list5 = ['hello', 'hello', 'hello']
list5.count('h')   # 0 
list5.count('hello')   # 3 
len(list5)      # 3 number of objects not letters separately 

list6 = [1, 2 [3, 4, 5], 6, 7, [8, 9, 10]]
len(list6)     # 6 

# extend(list) - расширяет список засчет другого списка - merges elements of first list into second changing only first list 
list7 = [1, 2, 3]
list8 = [4, 5, 6]
list7.extend(list8)
print(list7)     # [1, 2, 3, 4, 6]
print(list8)     # [4, 5, 6]   remains the same unchanged 

list7.extend(['John', 'Aibek'])
# [1, 2, 3, 'John', 'Aibek']

# index(element) - to get index of certain element in our list 
list8.index(3)      # 3 

list9 = [1, 2, 3, 4, 1, 2, 3, 5, 4, 1]
list9.index(1)     # 0 index of requested value 1 is 0 


# insert добавляет элемент по индексу list.insert(index, obj)
# insert(index, element)

# methods lets us to include value into our dictionary from any location versus append method that works only from the last value 

list10 = [ 1, 2, 3]
list10.insert(0, 'hello')    # inserts 'hello' under index 0 which means in the first place 
print(list10)     # ['hello', 1, 2, 3]
list10.insert(2, 10)     # ['hello', 1, 10, 2, 3] - inserts value 10 under index 2 
list10.insert(100, 'bye')  # ['hello', 1, 10, 2, 3, 100]  since there is no index 100 insert method includes the value in the last place 

users = ['John', 'Alex', 'Max', 'Karl']
users.insert(1, 'Rachel')   
# ['John', 'Rachel', 'Alex', 'Max', 'Karl']


# pop(index) by default pop has index -1 
# returns value of deleted value in list 
# in other words pop removes elements following their index and prints it out 

list0 = [1, 2, 3, 4, 5, 6, 7]
popped = list0.pop()     # deletes last element in list 
print(list0, popped)      # [1, 2, 3, 4, 5, 6] 7

popped = list0.pop(1)
print(list0, popped)     # [1, 3, 4, 5, 6]  2 

print([1, 2, [3, 4, [5, 6]]].pop(2).pop(2).pop(1))

# remove(element) method

users = ['John', 'Alex', 'Max', 'John', 'Karl'] # removes element and then prints out - deletion is only one time 
users.remove('John')
# ['Alex', 'Max', 'John', 'Karl']

if 'John' in users: 
    users.remove('John')
else:
    pass    # ничего не делай оставить все как есть 

remlist = [1, 2, 3, 4, 4, 5, 6, 7]
remlist.remove(2)
print(remlist)     # removes first element with value 2 

# map function returns our string into integers becasue we requested int map(int, str)
print(list(map(int, str(list).replace(', 2', '').replace(',', '').replace('[', '').replace(']', '').replace(' ', '').split(''))))


# reverse()
# method - reverses values in our list in a reversed order 
list00 = [1, 2, 3, 4, 5]
print(list00.reverse())      # None
print(list00)                # [5, 4, 3, 2, 1]
new_list00 = list00[::-1]    # [1, 2, 3, 4, 5]

# sort(key) сортирует по возрастанию 
# method - sorts values in our list [values/ elements must be of the same type i.e. strings and strings; int and int]
list000 = [2, 1, 5, 6, 3, 0]
list00.sort()
print(list00)      # [0, 1, 2, 3, 5, 6]


# sort(key) 
# example using len
users = ['Alice', 'Thomas', 'Cat', 'Ann', 'Raychel']
users.sort(key=len)
print(users)
# сортирует только по количеству букв в слове не по алфавиту 
# ['Cat', 'Ann', 'Alice, 'Thomas', 'Raychel']


# reverse() 
# расставляет все элементы в обратном порядке
list000 = [2, 1, 5, 6, 3, 0]
list00.sort(reverse=True)     # [6, 5, 3, 2, 1, 0]  



# copy()
users1 = ['Tom', 'Bob', 'Ann']
users2 = users1.copy()


# functions 
# функции не изменяет наши объекты в списке 
# len()

# max(), min()
numbers = [2, 1, 4, 5, 6]
print(max(numbers))       # 6 
print(min(numbers))       # 1

# sum()
print(sum(numbers))       # 18

# sorted()
# возвращает отсортированный список 

numbers = [2, 1, 4, 5, 6]
print(sorted(numbers))
# [1, 2, 4, 5, 6]


# срезы - slices 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[1:4])
# [2, 3, 4]
print(my_list[2:-1:2])
# [3, 5, 7]


# ####################################################################
# content from platform 

numbers = []
numbers1 = list() 

print(type(numbers))
print(type(numbers1))

numbers4 = [1, 2, 3, 4]
numbers5 = list(['makers', 'bootcamp', True, 56])
print(type(numbers5))

values = [7, 7, 7, 7, 7, 7]
values1 = [7] * 6 


# range()
# 1. range(end)    # only 1 argument that becomes the last value of range 
num = list(range(10))     
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 2. range(start, end) value start is included and end value is not included in our range 
num = list(range(3, 10))
# [3, 4, 5, 6, 7, 8, 9]

# 3. range(start, end, step)   max number of arguments in range is 3 
num = list(range(1, 10, 2))
# [1, 3, 5, 7, 9]


# function for 
for i in range(1, 11):
    print(i ** 2)


# сравнение списков 
num1 = [1, 2, 3, 4, 5]
num2 = [1, 2, 3, 4, 5]
print(num1 == num2)      # True 

num1 = [1, 2, 3, 4, 9]
num2 = [1, 2, 3, 4, 5]
print(num1 > num2)      # True 


# перебор 
users = ['Kan', 'Jan', 'Dan', 'Fredcrick']
for user in users:
    print(user)

# prints every user separately 


users = [
    ['Tom', 23], 
    ['Bob', 32],
    ['Emily', 19]
]
print(users[0])
# ['Tom', 23]

print(users[0][0])
# Tom 

print(users[0][0][1])
# o from Tom ---> index 1 == letter o 

for list_ in users: 
    for element in list_:
        print(element, end = ' | ')
        # Tom | 23 | Bob | 34 | 19
    print()
    # Tom | 23 |
    # Bob | 34 | 