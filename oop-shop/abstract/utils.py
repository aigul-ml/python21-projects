def get_obj_or_404(model, attr, val):
    # in param - title, in val - title itself 
    # function will return obj or the 404 error when smth is not found
    found = False 

    # проходимся по этому объекту - чтобы достать значение по атрибуту используем getattr()
    for obj in model.objects: 
        obj_val = getattr(obj, attr)
        # getattr() достает наши атрибуты в виде строки 

        # obj_val == value, который мы передали - останавливаем цикл 
        if obj_val == val: 
            found = True 
            break


    if not found: 
        # вызываем ошибку
        raise Exception(f'404 {model.__name__} Not Found')  # вытащит название класса 

    # возвращаем объект 
    return obj