from pprint import pprint
from urls import urlpatterns


while True:
    _url = input("Bведите адрес: ")
    if _url == '\q':
        # what this code means? 
        break
    try:
        url, arg = _url.split("/")
    except ValueError:
        print("Enter a valid url")
        continue
    found = False
    for uri, view in urlpatterns:
        if url == uri.split("/")[0]:
            found = True
            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)
    if not found:
        print("404 Url Not found")