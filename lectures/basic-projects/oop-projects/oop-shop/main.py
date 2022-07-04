from models import User, Product, Comment

user1 = User('test@gmail.com', 'hello', 'female')

user1.registration('123456789', '123456789')
user1.login('123456789')
# print(user1.is_authenticated)
user1.login('123456789')
# print(user1.is_authenticated)

product1 = Product('IPhone', 123455, '...', 3)
# user1.logout()

comment1 = Comment(user1, product1, 'Very nice phone!')
print(comment1)