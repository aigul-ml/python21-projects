""" WEEK 4/ 12 """
"================ Работа с файлами ==================="
# open - функция, которая позволяет открыть файл
"=========Режимы=========="
# r  - read (только для чтения)
# w  - write (только для записи (сначала все из файла удаляется, а потом записывается))
# a  - append (дозапись (все новое добавляется в конец))
# x  - создает файл. если он уже существует - ошибка
# rb  - чтение в бинарном виде
# wb  - запись в бинарном виде
# ab  - дозапись в бинарном виде

"когда мы не указываем режим - по умолчанию чтение"
# open("test.txt")  FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

"когда мы открываем файл в режиме w - он создает пустой файл и потом туда записывает данные"
# open("test.txt", "w")    - создает пустой файл

"когда файла нет - он создает его"
# open("test.txt", "a")


"===================READ======================"
file = open("test.txt") # открываем файл в режиме чтения
res = file.read() # считаывет весь файл и возвращает строку
print(file.read(5)) # пустая строка, потому что каретка находится в самом конце файла
file.seek(0) # каретка переходит в индекс 0 (в начало файла)
print(file.read(5))  # 'hello' (считал 5 символов)
print(file.read(5))  # ' worl' (считал следующие символы)
print(file.tell())  # 10  (показывает текущее положение каретки)
file.readlines()  # ['d\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n', 'line3\n']
file.seek(0)
print(file.readlines()) # ['hello world\n', 'Makers Bootcamp\n', 'line1\n', 'line2\n', 'line3\n']
print(file.tell()) # 46
file.close()


"===================WRITE====================="
file = open("test.txt", "w") # открыл файл, почистил
# res = file.read()   io.UnsupportedOperation: not readable
# метод read нельзя использовать при режиме записи и дозаписи
file.write("hello world\n") # в файл записали строку hello world
file.write("Makers Bootcamp\n") # после этого продолжает писать строку Makers Bootcamp
file.writelines(["line1\n", "line2\n", "line3\n"]) # принимает список со строками и дозаписывает их в файл
file.close() # обязательно закрываем файл




"==============With================="
# with - конструкция, которая в начале конструкции вызывает метод __enter__, а в конце вызывает __exit__
class Test:
    def __enter__(self):
        print("Начало работы")
        return self
    
    def __exit__(self, *args, **kwargs):
        print("Конец работы")
    
    def hello(self):
        print("Hello world")

with Test() as test:
    test.hello()

# Начало работы
# Hello world
# Конец работы


file1 = open("test.txt", "w")
file1.write("hello")
file1.close()
file2 = open("test.txt", "w")
file2.write("world")
# file1.write("fdgirwsukgh")  # ValueError: I/O operation on closed file.
# потому что file1 мы закрыли
file2.close()


with open("test.txt", 'w+') as file:
    file.write("Hello world\nMakers\nBootcamp")
    file.seek(0)
    res = file.read()
    file.seek(0)
    file.write("New lines\n")
    file.write(res)

with open("test.txt") as file:
    print(file.read())
    print(file.closed) # False
print(file.closed) # True




"========= Работа с файлами ========"
# try:
#     # open открывает файл для чтения
#     file = open('file.txt')
#     # Метод read() считывает файл полностью
#     # output = file.read()
#     # readline() # читает только одну строку
#     # output = file.readline()
#     # output2 = file.readline()
#     # readlines() читает все строки, возвращает список 
#     # output = file.readlines()
#     # print(output)
    
#     # seeker - курсор, считывающий файл
#     # s1 = file.read()
#     # file.seek(0) # передвигаем курсор в начало
#     # s2 = file.read()
#     # print("s1: ", s1)
#     # print("s2: ", s2)

#     # lineL1 = file.readline()
#     # print("➡ lineL1 :", lineL1)
#     # line2 = file.readline()
#     # print("➡ line2 :", line2)

#     # Считывание всех строк
#     # for line in file.readlines():
#     #     print(line)
# except:
#     pass
# finally:
#     file.close()

# Контекстный мененджнер
# with open('file.txt') as file:
#     print(file.read())

# Типы открытия файлов
# r (read) - станлартный тип открытия, только для чтения, если файла нет, вызывает ошибку
# w (write) - тип открытия только для записи, если файла нет, создает его, стирает
# with open('write_file.txt', 'w') as file:
    # write() записывает строку в файл
    # file.write('hello everyone')
    # writelines() записвает элементы итерируемого объекта в файл, не добваляет \n автоматически
    # file.writelines(['Hello', 'World'])
    # Если нужно чтобы каждая строка начиналась с новой строки
    # file.write('\n'.join(['hello', 'world']))

# a (append) - Добавляет новые записи в конец файла
# with open('write_file.txt', 'a') as file:
#     file.write('Hello world')

# w+ --> read + write - открывает файл как для чтения, так и для записи, создает несуществуюший файл
# r+ --> read + write - открывает файл, если его нет, вызывает ошибку
# a+ --> append + read - открывает файл для записи в конец, при отсутствии файла создает его
# with open('non-exist-file.txt', 'w+'): pass
# x --> open non-existing file and writes our input

"========= Пакеты, Модули ========="
# import file_package
# file_package.sum_file()

# Один файл (file_package.py) - это пакет
# from file_package import sum_file, read_sum_file
# sum_file(5, 100)

# a = 10
# b = read_sum_file()
# print(a + b)

# Папка с пакетами - это модуль
import math
"""
CONTENT FROM PLATFORM
"""

file1 = open('makers.txt', 'r')
data = file1.read()
print(data)

# readline - reads 1 line only 
# readlines --> reads multiple lines 

file2 = open('bootcamp.txt', 'w')
print(file2.write('This is Makers Bootcamp\n'))
strings = ['One\n', 'Two\n', 'Three\n']
file2.writelines(strings)

# do not forget to close the file
file2.close()
print(file2.closed)

