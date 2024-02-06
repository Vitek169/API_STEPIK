import requests



"""Создаем класс"""
class PersonWithVedor:
    def __init__(self):
        pass


    def all_persons_in_films_with_Dart(self):
        """создаем  запрос для получения информации о Дарте Вейдоре"""
        url_dart = 'https://swapi.dev/api/people/4/'
        print(url_dart)

        result_url_dart = requests.get(url_dart)
        print(f'Информация о Дарте Вейдоре {result_url_dart.text}')
        result_films = result_url_dart.json()
        result_films_info = result_films.get('films')
        print(f'Ссылки на фильмы с Дартом {result_films_info}')

        """создаем цикл для запроса персонажей в фильмах"""
        for i in result_films_info:
            info = requests.get(i) #создаем запрос на фильмы
            result_films = info.json()
            result_name_films_info = result_films.get('title')
            result_character_info = result_films.get('characters')
            print(f'Названия фильма "{result_name_films_info}"')
            f = open('Character and films.txt', 'a')
            f.write(f"Название фильма: {result_name_films_info}.\n")
            f.close()
            """Создаем цикл для запроса имен персонажей в фильме и записи в файл"""
            for j in result_character_info:
                info_person = requests.get(j)
                result_name_character = info_person.json()
                result_name_character_info = result_name_character.get('name')
                print(f'Имя персонажа {result_name_character_info}\n')
                f = open('Character and films.txt', 'a')
                f.write(f'Имя персонажа: {result_name_character_info}\n')
                f.close()




all_person = PersonWithVedor()
all_person.all_persons_in_films_with_Dart()
