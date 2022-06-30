"============================ tuples ================================="
# кортежи - неизменяемые, индексируемый, упорядоченный, итерируемый тип данных предназначенный для хранения всех типов данных в определенном порядке. 
# в целом не отличается от списков - просто неизменяемый тип данных поэтому занимает меньше памяти 

tuple = ('hello', 2.5, 19, (2, 3), [1, 2, 3])
tuple[-1].append(4) 
tuple2 = tuple('hello')     # ('h', 'e', 'l', 'l', 'o')

tuple3 = 1, 2, 3   # (1, 2, 3)     # we can create tuple without round brackets 
tuple4 = (5)       # 5 
tuple5 = 5         # (5)
tuple6 = 'hello'   # ('h', 'e', 'l', 'l', 'o')
tuple7 = tuple([1, 2, 3])      # (1, 2, 3)

# python - динамически типизированный язык - он понимает какой тип данных 

"============================ tuple methods ================================="
# count - counts requested element in our tuple 
tuple0 = (1, 2, 3, 4, 1, 1, 1)
tuple0.count(1)     # 4
tuple0.count(2)     # 1 

# index - to get index of certain element in our list 
tuple0.index(3)      # 3 

tuple9 = [1, 2, 3, 4, 1, 2, 3, 5, 4, 1]
tuple9.index(1)     # 0 index of requested value 1 is 0 
