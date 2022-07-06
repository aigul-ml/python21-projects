#   ПОЛИМОРФИЗМ
# принцип ООП, в кот методы в разных классах называются одинаково (один интерфэйс - разный функционал)

class Dog:
    def speak(self):
        print("гав-гав")

class Cat:
    def speak(self):
        print("мяу-мяу")

animals = [Cat(),Dog(),Dog()]

for animal in animals:
    animal.speak()
    
print(dir(str))
print(dir(list))
print(dir(dict))
print(dir(int()))

# len method

# __add__
# 'a' + 'b' = 'ab'
# [1, 2, 3] + [4, 5, 6]
# {'a': 2} + {'b': 4}
