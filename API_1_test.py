import requests

"""Создаем метод, который отправляет get запрос на получение списка категорий и  возвращает его в виде списка"""
url_category = 'https://api.chucknorris.io/jokes/categories'
print(url_category)
value_url_category = requests.get(url_category)
print(f'Список категорий {value_url_category.text}')
print(f'Статус код:{value_url_category.status_code}. Запрос успешен!')


class ChukJoke:

    def __int__(self):
        pass

    """Создаем метод, в теле которого находится цикл"""
    def counter(self):
        for category in value_url_category.json(): #Цикл проходящий по списку категорий шуток
            url = f'https://api.chucknorris.io/jokes/random?category={category}' #Рот каждой новой итерации подставляется категория в тело запроса
            result = requests.get(url) #Отправка запроса
            print(f'Статус код: {result.status_code}, Внимание! Шутка! {result.json()}') #Получение статус кода и шутки в формате .json
            assert result.status_code == 200
            print('Шутка успешно получена')


jokechack = ChukJoke()
jokechack.counter()