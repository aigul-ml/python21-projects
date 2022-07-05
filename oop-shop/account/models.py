import permissions

class User: 
    objects = [] # adding objects into list 

    def __init__(self, email, name, sex) -> None:
        self.email = email 
        self.name = name 
        self.sex = sex 
        self.__password = None
        self.is_authenticated = False
        print(f'Success - user is created {self.email}')
        # to objects adding object to our empty list of objects on line 4 [objects = [] ]
        User.objects.append(self)

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