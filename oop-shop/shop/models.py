from audioop import add
import permissions 

class Category: 
    objects = []

    def __init__(self, title) -> None:
        self.title = title

        Category.objects.append(self)

    def __str__(self) -> str:
        return self.title

class Product: 
    objects = []
    _id = 0

    def __init__(self, title, price, description, quantity, category) -> None:
        self.id = Product._id   # записывает id продукта
        self.title = title 
        self.price = price
        self.desc = description
        self.quant = quantity
        self.category = category

        Product.objects.append(self)
        Product._id += 1   # записывает +1 -- допустим ıd было 0 затем стало 1 и т.д.

    def __str__(self) -> str:
        return f'{self.title} [{self.quant}] - {self.price}\n({self.desc[:20]})'

class Comment: 
    objects = []

    def __init__(self, user, product, body) -> None:
        permissions.login_required(user)   # only logged in users can leave a comment 
        from datetime import datetime
        self.user = user 
        self.product = product
        self.body = body
        self.created_at = datetime.now()

        Comment.objects.append(self)

    def __str__(self) -> str:
        return f'{self.user.email} - [{self.created_at}] - {self.body}'