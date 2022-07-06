# views - functions to cooperate with our serializers
from abstract.utils import get_obj_or_404

from unicodedata import category
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer


def product_list(): 
    serializer = ProductSerializer()  # создаем объект сериализатора
    
    # просим список всех наших продуктов
    products = serializer.serialize_queryset()    # не передаем ничего - поэтому вернет всё
    return products

def product_create(): 
    title = input('Enter title of the product: ')
    price = input('Enter price of product: ')
    desc = input('Enter description: ')
    quant = input('Enter quantity: ')

    print('Choose category: ')
    # вызываем нашу категорию и выводим

    for cat in Category.objects:
        print(cat.title)
    cat_title = input('""""""""""""""""""""""""\n')

    category = get_obj_or_404(Category, 'title', cat_title)
    Product(title, price, desc, quant, category)
    return 'Продукт успешно создан'


def product_detail(p_id): 
    product = get_obj_or_404(Product, 'id', int(p_id))
    # int(p_id) потому что нам нужны числа
    serializer = ProductSerializer()
    return serializer.serialize_obj(product)

def product_delete(p_id): 
    product = get_obj_or_404(Product, 'id', int(p_id))
    Product.objects.remove(product)
    return 'Продукт успешно удален'

def product_update(p_id):
    product = get_obj_or_404(Product, 'id', int(p_id))
    field = input('Enter field for changes: ')
    if field in dir(product):
        print(f'old value: {getattr(product, field)}')
        value = input(f'{field} = ')
        setattr(product, field, value)
    else:
        raise Exception(f'Поля {field} нет в продукте.')
        
        
    return product_detail(p_id) 

    