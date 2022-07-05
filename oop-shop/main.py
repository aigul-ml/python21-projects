from pprint import pprint 
from shop.models import Product
from abstract.serializers import BaseSerializer

obj1 = Product('IPhone', 234, '...', 3)
obj2 = Product('lenovo', 34, '...', 2)
obj3 = Product('samsung', 32, '...', 2)

res = BaseSerializer().serialize_queryset([obj1, obj2, obj3])
pprint(res)

# user1 = User('test@gmail.com', 'hello', 'female')

# user1.registration('123456789', '123456789')
# user1.login('123456789')
# # print(user1.is_authenticated)
# user1.login('123456789')
# # print(user1.is_authenticated)

# product1 = Product('IPhone', 123455, '...', 3)
# # user1.logout()

# comment1 = Comment(user1, product1, 'Very nice phone!')
# print(comment1)