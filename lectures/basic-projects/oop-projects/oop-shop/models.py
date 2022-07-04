from audioop import add
import permissions 


class Category: 
    def __init__(self, title) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title

class Product: 
    def __init__(self, title, price, description, quantity) -> None:
        self.title = title 
        self.price = price
        self.desc = description
        self.quant = quantity

    def __str__(self) -> str:
        return f'{self.title} [{self.quant}] - {self.price}\n({self.desc[:20]})'

class Comment: 
    def __init__(self, user, product, body) -> None:
        permissions.login_required(user)   # only logged in users can leave a comment 
        from datetime import datetime
        self.user = user 
        self.product = product
        self.body = body
        self.created_at = datetime.now()

    def __str__(self) -> str:
        return f'{self.user.email} - [{self.created_at}] - {self.body}'

class User: 
    def __init__(self, email, name, sex) -> None:
        self.email = email 
        self.name = name 
        self.sex = sex 
        self.__password = None
        self.is_authenticated = False
        print(f'Success - user is created {self.email}')

    def registration(self, password, password_confirm): 
        if password != password_confirm: 
            raise Exception("Passwords are not matching.")
        self.__password = password  # we can reach this object only within this class outside of this class - object is not available - __ (double underscore)
        print(f'Success - user is registered {self.email}')

    def login(self, password): 
        if self.__password != password:
            raise Exception('Password is not correct.')
        self.is_authenticated = True
        print(f'Success - user is logged in {self.email}')

# user1 = User('hello@gmail.com', 'hello', 'f')
# user1.registration('123456789', '123456789')
# print(user1.password)    

    def logout(self): 
        permissions.login_required(self)
        self.is_authenticated = False
        print(f'Success - user {self.email}')

    def __str__(self) -> str:  # prints out and shapes the string in a more esthetic way 
        return self.email