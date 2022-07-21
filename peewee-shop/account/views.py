from .models import MyUser


def register():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    MyUser.create(username=username, password=password)
    return "User has been created."