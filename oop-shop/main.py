# from shop.models import Product, Category
# from shop.views import product_list, product_update

# cat = Category("phones")
# Category('dyson')
# Category('food')
# Product("iphone", 234, "...", 3, cat)
# Product("lenovo", 32, "...", 5, cat)
# Product("samsung", 76, "...", 10, cat)


# # res = ProductSerializer().serialize_queryset([obj1, obj2, obj3])
# from pprint import pprint
# pprint(product_list())
# # while True: 
# #     id_ = input('Enter id of product: ')
# #     pprint(product_detail(id_))
# id_ = input('Enter product for changes: ')
# pprint(product_update(id_))
# # pprint(product_list())



# # user1 = User('test@gmail.com', 'hello', 'female')

# # user1.registration('123456789', '123456789')
# # user1.login('123456789')
# # # print(user1.is_authenticated)
# # user1.login('123456789')
# # # print(user1.is_authenticated)

# # product1 = Product('IPhone', 123455, '...', 3)
# # # user1.logout()

# # comment1 = Comment(user1, product1, 'Very nice phone!')
# # print(comment1)


from urls import urlpatterns
from pprint import pprint

while True:
    try:
        url, arg = input("Введите адрес: ").split("/")
    except ValueError:
        print("Enter a valid url")
        continue

    found = False
    for uri, view in urlpatterns:
        if uri.split("/")[0] == url:
            found = True

            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)

    if not found:
        print("404 Url Not Found")