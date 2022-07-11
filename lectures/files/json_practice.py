"""
JSON
COntent from platform

dump(), dumps()
"""
import json

info = {
    "name": "Alice", 
    "age": 79,
    "book": "Chamber of Secret"
}

with open('info.json', 'w') as my_file: 
    json.dump(info, my_file)


"""
load(), loads()
"""
with open('info.json') as my_file: 
    python_object = json.load(my_file)
    print(python_object)
    # {'name': 'Alice', 'age': 79, 'book': 'Chamber of Secret'}

python_object['name'] = 'John'
print(python_object)

with open('info.json', 'w') as my_file: 
    json.dump(python_object, my_file)


json_str = '{"name": "Alice", "age": 79, "book": "Chamber of Secrets"}'
# из формата json получить python object --> десериализовать наши данные 
py_object = json.loads(json_str)

print(json_str)
# {"name": "Alice", "age": 79, "book": "Chamber of Secrets"}
print(py_object)
# {'name': 'Alice', 'age': 79, 'book': 'Chamber of Secrets'} --> dictionary


# Example with Harry Potter
with open('HarryPotterBooks.json') as file9: 
    dictionary = json.load(file9)
    # deserializatsiia from json format into python object
    # output --> dictionary

    data = dictionary['books']

    for book in data:
        book['author'] = 'J.K.Rowling'
        # добавление новой пары - ключ: значение
    
    print(dictionary)


# updating our json
with open('HarryPotterBooks.json', 'w') as file9: 
    json.dump(dictionary, file9)
     