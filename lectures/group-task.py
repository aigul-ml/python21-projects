# # # task 1 
# # from re import A
# # from math import sqrt

# # def func(): 
# #     a = int(input('Enter a: '))
# #     perimetr = a ** 2
# #     kvadrat = a ** 3 
# #     diagonal = sqrt(a**2)
# #     return perimetr, kvadrat, diagonal
# # print(func())



# # task 3 
# # a = 1234
# # for i in a.split():

# list_ = [1234]
# new_list = []

# string = list_.pop()

# if len(int) % 2 > 0:
#     new_list.extend(int[len(int) // 2 + 1:])
#     new_list.extend(int[:len(int) // 2 + 1])
# else:
#     new_list.extend(int[len(int) // 2:])
#     new_list.extend(int[:len(int) // 2])

# print(new_list)


# def sum_digits(n):
#     sum = 0
#     for digit in str(n):
#         if max(int(digit)):
#            digit.replace(min) 
#     return sum
# print(sum_digits(1234))


# def max_min(digit = 1234): 
#     if max(digit) in int(digit):
#         print(max(int(digit)))
#     #     replace(min(digit))
    # else: 


# task 3
num = 4321
num1 = int(str(num)[0])
num2 = int(str(num)[1])
num3 = int(str(num)[2])
num4 = int(str(num)[3])
if num1 > num2 and num2 > num3 and num3 > num4: 
    print('Yes')
else:
    print('No')


num = 4331
numbers = [int(i) for i in str(num)]
sorted_numbers = numbers.copy()
sorted_numbers.sort(reverse=True)
if numbers == sorted_numbers:
    print("yes")
else:
    print("no")