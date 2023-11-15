import requests

"""Создаем запрос для получения всех доступных категорий"""

url_category = 'https://api.chucknorris.io/jokes/categories'
print(url_category)
result_url_category = requests.get(url_category)
print(f'Все категории доступные к запросу- {result_url_category.text}')
value_category = result_url_category.text
"""Проверяем,все ли категории выгрузились по списку"""

assert '["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"]' == value_category
print('Все категории присутствуют')


class CategoryChuck:

    def __int__(self):
        pass

    """Создаем бесконечный цикл для запроса категории"""
    def category_for_users(self):
        while True:
            user_category = input('Введите катeгорию из списка: ')
            if user_category in value_category:
                print('Данная категория присутствует в списке!')
                result_user_category = requests.get(f'https://api.chucknorris.io/jokes/random?category={user_category}')
                print(f'Шутка с категории {user_category}: {result_user_category.json()}')
                assert 200 == result_user_category.status_code
                print('Шутка найдена успешно!')

            else:
                print('Данной категории в списке нет. Введите снова')




"""Создаем объект класса"""
user_cat = CategoryChuck()
user_cat.category_for_users()
