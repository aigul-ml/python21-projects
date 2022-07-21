from .models import Comment, Product
from .serializers import ProductSerializer
from account.models import MyUser


def create_product():
    category = input("Please enter category: ")
    title = input("Please enter title: ")
    price = float(input("Please enter price: "))
    description = input("Please enter description: \n")
    Product.create(category=category, title=title, price=price, description=description)
    return "Product has been created."

def product_list():
    return ProductSerializer().serialize_queryset()

def create_comment(p_id):
    from datetime import datetime
    username = input("Please enter username: ")
    user = MyUser.get(username=username)
    # ищи по вот этому username
    
    product = Product.get_by_id(p_id)
    body = input("Please enter comment: ")
    created_at = datetime.now()
    Comment.create(user=user, product=product, body=body, created_at=created_at)
    return "Comment has been created."