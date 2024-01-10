import requests
base_url = 'https://rahulshettyacademy.com' #Базовая url
key = '?key=qaclick123' #Параметры для всех звапросов
post_resource = '/maps/api/place/add/json' #Ресурс метода Post

'''Создание метода post'''
post_resource = '/maps/api/place/add/json' #Ресурс метода Post
class TestNewLoc():
    '''Работа с новой локацией'''

    def __int__(self):
        pass

    def test_create_new_loc(self):
        '''Создание новых локаций'''
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


    def test_get_new_loc(self):
        """Метод для отправки запроса GET и получение запроса о создании новой локации"""

        get_resource = '/maps/api/place/update/json'
        f = open('placeID.txt', 'r')
        for i in f:
            get_url = base_url + get_resource + key + '&place_id=' + i
            print(get_url)
            result_get = requests.get(get_url)
            print(result_get.text)
            print(result_get.status_code)
            assert 200 == result_get.status_code
            print('Проверка создания новой локации прошла успешно!')
        f.close()

    def test_delete_new(self):
        """Метод для удаления длкации"""
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        with open('placeID.txt') as f:
            l = f.read().splitlines()
        print(l)
        new_l = [l[1], l[3]] #Созжаю список из 2ух элементов
        print(new_l)
        for i in new_l: #Прохожу циклом по этим двум элементам и добавляю их в place_id
             json_for_delete_new_location = {
                "place_id": i

            }

        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)
        print(result_delete.status_code)
        result_delete_status = result_delete.json()
        info_result_delete_status = result_delete_status.get('status')
        print(f'Статус: {info_result_delete_status}')
        assert info_result_delete_status == 'OK'
        print('Удалена новая локация!')

        '''Проверяем удалилась ли локация'''
        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + i
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Статус код: {result_get.status_code}")
        assert 404 == result_get.status_code
        print('Проверка удаления локации прошла успешно!')
        check_delete = result_get.json()
        check_delete_info = check_delete.get('msg')
        assert check_delete_info == "Get operation failed, looks like place_id  doesn't exists"
        print('Локация не обнаружена!')
        l.pop(1)# Удаляем элементы из списка
        l.pop(2)
        """Созжаем новыйй список с оставшимися локациями"""
        with open('placeID_new.txt.', 'w') as filehandle:
            for listitem in l:
                filehandle.write('%s\n' % listitem)


        print('Тестирование Test_new_locathion - завершено!')


new_place = TestNewLoc()
new_place.test_create_new_loc()
new_place.test_get_new_loc()
new_place.test_delete_new()