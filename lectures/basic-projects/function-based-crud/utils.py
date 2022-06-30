# Файл с дополнительными функциями 

from shutil import ExecError


def generate_id(ids):
    """
    Принимает список существующих id
    Возвращает новое id в диапазоне от 100 до 1000
    """
    import random
    id_ = random.randint(100, 1000)
    while id_ in ids: 
        id_ = random.randint(100, 1000)
    return str(id_) 

def validate_password(p1, p2):
    """
    Принимает 2 пароля 
    Если они не совпадают - вызывается ошибка

    """
    if p1 != p2:
        raise Exception('Passwords are not matching!')
    
def validate_id(ids, u_id): 
    '''
    Принимает список существующих id и id, которое нужно проверпить
    Если такого id нет в списке - вызывается Exception
    '''
    if u_id in ids: 
        raise Exception('There is no such user.')


def read_db(name):
    '''
    Принимает название файла
    Возвращает данные из базы данных в виде python objects
    '''
    import json
    with open(name, 'r') as file: 
        db = json.load(file)
    return db 

def write_to_db(name, data): 
    '''
    Принимает название файла и данные для записи
    Записывает эти данные в файл
    '''
    import json 
    with open(name, 'w', encoding='utf8') as file: 
        # dump method writes our data 
        json.dump(data, file, ensure_ascii=False)