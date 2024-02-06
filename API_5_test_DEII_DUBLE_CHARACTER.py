import requests
import os

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

        """Проходим по списку с фильмами"""
        for i in result_films_info:
            info = requests.get(i)  # создаем запрос на фильмы
            result_films = info.json()
            result_name_films_info = result_films.get('title')
            print(f'Название фильма: {result_name_films_info}')
            f = open('Films and cherecter.txt', 'a') # Записываем название фильма в файл
            f.write(f"Название фильма: {result_name_films_info}.\n")

        """Проходим по списку с фильмами"""
        for j in result_films_info:
            info = requests.get(j)  # создаем запрос на фильмы
            result_films = info.json() # Выводим в формате json
            info_character = result_films.get('characters')

            """Проходим по списку с персонажами"""
            for k in info_character:
                info_character_films = requests.get(k)
                resulult_info_character_films = info_character_films.json()
                all_resulult_info_character_films = resulult_info_character_films.get('name') # создаем запрос на имя персонажа
                print(f'Имя персонажа - {all_resulult_info_character_films}')
                f = open('Films and cherecter.txt', 'a') # Записываем имя персонажа в файл
                f.write(f"Имя персонажа, который присутствовал в фильме вместе с Дартом Вейдером: {all_resulult_info_character_films}.\n")
                f.close() # Закрываем файл

        """Создаю метод лдя удаления двойных имен путем проверки созданного файла, и созданием нового файла, без дублирующих имен"""
    def dell_duble_name(self):
        result_name_character_info = set()
        with open(r"Films and cherecter.txt", "r") as fin, open(r"Films and cherecter all.txt", "w") as fout:
            for line in fin:
                if line not in result_name_character_info:
                    fout.write(line)
                result_name_character_info.add(line)
        os.remove("Films and cherecter.txt")



all_person = PersonWithVedor()
all_person.all_persons_in_films_with_Dart()
all_person.dell_duble_name()