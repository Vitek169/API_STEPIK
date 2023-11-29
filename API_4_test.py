import requests
base_url = 'https://rahulshettyacademy.com' #Базовая url
key = '?key=qaclick123' #Параметры для всех звапросов

'''Создание метода post'''
post_resource = '/maps/api/place/add/json' #Ресурс метода Post
class TestNewLoc():
    '''Работа с новой локацией'''

    def __int__(self):
        pass

    def test_create_new_loc(self):
        '''Создание новых локаций'''
        base_url = 'https://rahulshettyacademy.com'  # Базовая url
        key = '?key=qaclick123'  # Параметры для всех звапросов
        # '''Создание метода post'''
        post_resource = '/maps/api/place/add/json'  # Ресурс метода Post
        post_resource = '/maps/api/place/add/json'  # Ресурс метода Post
        for i in range(5): # Создаем цикл
            base_url = 'https://rahulshettyacademy.com' #Базовая url
            key = '?key=qaclick123' #Параметры для всех звапросов

            '''Создание метода post'''
            post_url = base_url + post_resource + key
            print(post_url)
            json_for_create_new_locathion = {
                "location": {

                    "lat": -38.383494,

                    "lng": 33.427362

                }, "accuracy": 50,

                "name": "Frontline house",

                "phone_number": "(+91) 983 893 3937",

                "address": "29, side layout, cohen 09",

                "types": [

                    "shoe park",

                    "shop"

                ],

                "website": "http://google.com",

                "language": "French-IN"

            }


            result_post = requests.post(post_url, json = json_for_create_new_locathion) #создаем переменную, куда указываем тип запроса, в данном случае post, в теле указываем данные, которые передаем, а именно базовую url и тело json в формате json
            print(result_post.text)

            assert 200 == result_post.status_code
            print('Создана новая локация')
            check_post = result_post.json() #Создаем переменную куда вносим результат запроса post в формате json
            place_id = check_post.get('place_id')
            f = open('placeID.txt', 'a') #создаем переменную, в которой вписываем данные что нужно делать с файлом. в конуретном случае открываем указанный в скобке файл, для добавления информации в конец файла
            f.write(f"{place_id} {'\n'}") #Записываем в файл place_id, и перенос на следующую строку
            f.close() #Закрываем файл

        get_recource = '/maps/api/place/update/json'
        f = open('placeID.txt', 'r')
        for i in f:
            get_url = base_url + get_recource + key + '&place_id=' + i
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            print(result_get.status_code)
            assert 200 == result_get.status_code
            print('Проверка создания новой локации прошла успешно!')
        f.close()






new_place = TestNewLoc()
new_place.test_create_new_loc()


