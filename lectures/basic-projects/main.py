# database = {
#     "Бекзат": "скала",
#     "Эртай": "пароль",
#     "Оомат": "Кыргызстан",
#     "Имран": "12345",
#     "Жийде": "return",
#     "Манас": "Маке",
#     "Арафат": "54321",
#     "Элжаз": "парол",
#     "Гулсана": "312",
#     "Эркайым": "Айдин",
#     "Бекназ": "Арёль",
#     "Эдиль": "ьлорап",
#     "Айгул": "май",
#     "Закир": "@@@",
#     "Бегайым": "makers",
#     "Мырзайым": "Bootcamp2221",
#     "Даниэл": "covid19",
#     "Жибек": "1404",
#     "Айгерим":"moon02",
#     "Калысбек": "стол",
#     "Ырыс": "suuuuuuuuiiiiiiiiiiii",
#     "Айканыш": "qwerty",
#     "Арген": "11172332",
#     "Нурмухамед": "Не верный",
#     "Бектур": "0101",
#     "Алан": "душу питона",
#     "Жаангер": "ох блин",
#     "Богдан": "Кудайберген",
#     "Айгерим": "синий маркер",
#     "Настя": "Python21"
# }

# import random

# ids = []

# for key, value in database.copy().items():
#     id = random.randint(100, 999)
#     while id in ids:
#         id = random.randint(100, 999)
#     ids.append(id)

#     database[id] = {
#         'name': key,
#         'password': value,
#         'info': '...'
#     }
#     del database[key]
# print(database)

from xml.dom import ValidationErr
from utils import validate_id, read_db, write_to_db


database = read_db(db.json)
# {
#     377: {'name': 'Бекзат', 'password': 'скала', 'info': '...'}, 
#     769: {'name': 'Эртай', 'password': 'пароль', 'info': '...'}, 
#     933: {'name': 'Оомат', 'password': 'Кыргызстан', 'info': '...'}, 
#     739: {'name': 'Имран', 'password': '12345', 'info': '...'}, 
#     463: {'name': 'Жийде', 'password': 'return', 'info': '...'}, 
#     583: {'name': 'Манас', 'password': 'Маке', 'info': '...'}, 
#     707: {'name': 'Арафат', 'password': '54321', 'info': '...'}, 
#     451: {'name': 'Элжаз', 'password': 'парол', 'info': '...'}, 
#     194: {'name': 'Гулсана', 'password': '312', 'info': '...'}, 
#     305: {'name': 'Эркайым', 'password': 'Айдин', 'info': '...'}, 
#     589: {'name': 'Бекназ', 'password': 'Арёль', 'info': '...'}, 
#     255: {'name': 'Эдиль', 'password': 'ьлорап', 'info': '...'}, 
#     496: {'name': 'Айгул', 'password': 'май', 'info': '...'}, 
#     246: {'name': 'Закир', 'password': '@@@', 'info': '...'}, 
#     356: {'name': 'Бегайым', 'password': 'makers', 'info': '...'}, 
#     978: {'name': 'Мырзайым', 'password': 'Bootcamp2221', 'info': '...'}, 
#     899: {'name': 'Даниэл', 'password': 'covid19', 'info': '...'}, 
#     644: {'name': 'Жибек', 'password': '1404', 'info': '...'}, 
#     440: {'name': 'Айгерим', 'password': 'синий маркер', 'info': '...'}, 
#     270: {'name': 'Калысбек', 'password': 'стол', 'info': '...'}, 
#     529: {'name': 'Ырыс', 'password': 'suuuuuuuuiiiiiiiiiiii', 'info': '...'}, 
#     471: {'name': 'Айканыш', 'password': 'qwerty', 'info': '...'}, 
#     317: {'name': 'Арген', 'password': '11172332', 'info': '...'}, 
#     838: {'name': 'Нурмухамед', 'password': 'Не верный', 'info': '...'}, 
#     649: {'name': 'Бектур', 'password': '0101', 'info': '...'}, 
#     953: {'name': 'Алан', 'password': 'душу питона', 'info': '...'}, 
#     211: {'name': 'Жаангер', 'password': 'ох блин', 'info': '...'}, 
#     935: {'name': 'Богдан', 'password': 'Кудайберген', 'info': '...'}, 
#     797: {'name': 'Настя', 'password': 'Python21', 'info': '...'}}

def read(u_id):
    """
    Принимает id юзера 
    Выводит его имя и информацию 
    Если такого юзера нет - вызывается Exception
    """
    validate_id(database.keys(), u_id)
    name = database[u_id]['name']
    info = database[u_id]['info']
    sex = database[u_id]['sex']
    print(f'''
    ======{u_id}======
    Name: {name}
    Info: {info}
    ''')
read(935)


def create():
    '''
    Запрашивает данные о пользователе
    Записывает в базу данных 
    '''
    from utils import generate_id, validate_password
    name = input('Enter your name: ')
    password = input('Enter your password: ')
    password2 = input('Confirm your password: ')
    validate_password(password, password2)
    info = input('Enter information about yourself: ')
    sex = input('Identify your gender (m, f): ')
    id_ = generate_id(database.keys())
    database[id_] = {
        'name': name,
        'password': password,
        'info': info
        'sex': sex
    }

    print('You have been successfully added into our database.')

def delete(u_id):
    '''
    Принимает id пользователя
    Если юзер существует - он удаляется из базы данных
    Если юзера нет - вызывается ошибка 
    '''
    validate_id(database.keys(), u_id)
    name = database[u_id]
    sex = database[u_id]['sex']
    del database[u_id]
    if sex == 'm': 
        print(f'{name} has been successfully deleted.')
    else: 
        print(f'{name} has been successfully deleted.')
    print(f'{u_id} was successfully deleted.')

delete(797)
print(database)

def update(u_id): 
    '''
    Принимает id юзера
    Выводит старые данные 
    Принимает новые данные 
    Перезаписывает в базу данных 
    '''
    validate_id(database.keys(), u_id)
    read(u_id)
    # принимаем новые данные 
    name = input('Enter your name: ')
    info = input('Enter information about yourself: ')
    sex = input('Enter your gender: ')

    database[u_id]['name'] = name
    database[u_id]['info'] = info
    database[u_id]['sex'] = sex
    read(u_id)

update(933)