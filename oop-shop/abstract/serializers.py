from dataclasses import fields
from shop.models import Product


class BaseSerializer: 
    class Meta: 
        fields = []   # поля ['title', 'price', 'desc']
        queryset = []

# BaseSerializer.Meta.fields  - calling our class via meta class 

    def serialize_obj(self, obj): 
        fields = self.Meta.fields
        dict_ = {}
        for field in fields:  # проходимся по полям 
            # obj.title - мы можем обращаться к атрибуту getattr
            # getattr(obj, 'title')
            dict_[field] = getattr(obj, field)   # adding to our dictionary 
        return dict_
    
    def serialize_queryset(self, queryset=None): 
        if queryset is None: 
            queryset = self.Meta.queryset
            
        list_ = []
        for obj in queryset: 
            dict_ = self.serialize_obj(obj)
            list_.append(dict_)
        return list_
 
# obj = Product('IPhone', 234, '....', 3)   --> getting our dictionary from object items 
# res = BaseSerializer().serialize_obj(obj)
# print(res)