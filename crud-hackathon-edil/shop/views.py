from unicodedata import decimal
from .models import Cars



class ProductSerializer:
    class Meta:
        fields = ["id","marka", "model", "year", "volume", "color", "cuzov", "probeg", "price"]
        queryset = Cars.objects

    def serialize_obj(self, obj):
        fields = self.Meta.fields
        dict_ = {}
        for field in fields:
            
            dict_[field] = getattr(obj, field)
        return dict_
    

def cars_create():
    marka = input("Введите название марки: ")
    model = input("Введите название модели: ")
    year = int(input("Введите год выпуска: "))
    volume = float(input("Введите обьем двигателя: "))
    color = input("Введите цвет машины: ")
    cuzov = input(f"Введите тип кузова {Cars.cuzov}: ")
    price = float(input("Введите стоимость: "))
    probeg = int(print("Введите пробег: "))
    Cars(marka, model, year, volume, color, cuzov, probeg, price)
    return "Продукт успешно создан"

def get_obj_or_404(model, attr, val):
    found = False

    for obj in model.objects:
        obj_val = getattr(obj, attr)
        if obj_val == val:
            found = True
            break

    if not found:
        raise Exception(f"404 {model.__name__}  Not Found")
    return obj

def cars_detail(p_id):
    product = get_obj_or_404(Cars, "id", int(p_id))
    serializer = ProductSerializer()
    return serializer.serialize_obj(product)

def cars_update(p_id):
    product = get_obj_or_404(Cars, "id", int(p_id))
    field = input("Введите поле для изменения: ")
    if field in dir(product):
        print(f"old value: {getattr(product, field)}")
        value = input(f"{field} = ")
        setattr(product, field, value)
    else:
        raise Exception(f"Поля {field} нет в продукте")
    return cars_detail(p_id)

def cars_delete(p_id):
    product = get_obj_or_404(Cars, "id", int(p_id))
    Cars.objects.remove(product)
    return "Продукт успешно удален"