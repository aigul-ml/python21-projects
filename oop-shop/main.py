from shop.models import Product, Category
from shop.serializers import ProductSerializer

cat = Category("phones")
obj1 = Product("iphone", 234, "...", 3, cat)
obj2 = Product("lenovo", 32, "...", 5, cat)
obj3 = Product("samsung", 76, "...", 10, cat)

res = ProductSerializer().serialize_queryset([obj1, obj2, obj3])
from pprint import pprint
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