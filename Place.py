import requests

class Test_new_locathion():
    """Работа с новой локацией"""

    def __int__(self):
        pass

    def test_create_new_locathion(self):
        """Создание новой локации"""

        base_url = 'https://rahulshettyacademy.com' #Базовая url
        key = '?key=qaclick123' #Параметры для всех звапросов

        '''Создание метода Post'''
        post_resource = '/maps/api/place/add/json' #Ресурс метода Post

        post_url = base_url + post_resource + key
        print(post_url)

        json_for_create_naw_location = {
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

        result_post = requests.post(post_url, json = json_for_create_naw_location)
        print(result_post.text)
        assert 200 == result_post.status_code
        print('Создана новая локация')
        check_post = result_post.json()
        check_info_post = check_post.get('status')
        print(f'Статус код ответа: {check_info_post}')
        assert check_info_post == 'OK'
        print('Статус ответа верен')

        place_id = check_post.get('place_id')
        print(f'Place = id: {place_id}')

        """Проверка создания новой локации"""
        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(result_get.status_code)
        assert 200 == result_get.status_code
        print('Проверка создания новой локации прошла успешно!')

        """Изменение новой локации"""
        put_recource = '/maps/api/place/update/json'
        put_url = base_url + put_recource + key
        print(put_url)
        json_for_updat_naw_location = {
            "place_id": place_id,

            "address": "100 Lenina street, RU",

            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json = json_for_updat_naw_location)
        print(result_put.text)
        print(f'Статус код: {result_put.status_code}')
        assert 200 == result_put.status_code
        print('Изменения внесены')
        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print(f'Сообщение: {check_put_info}')
        assert check_put_info == 'Address successfully updated'
        print('Сообщение врно')

        """Проверка обнавления локации"""
        result_get = requests.get(get_url)
        print(result_get.text)
        print(result_get.status_code)
        assert 200 == result_get.status_code
        print('Проверка обнавления локации прошла успешно!')
        check_address = result_get.json()
        check_address_info = check_address.get('address')
        assert check_address_info == '100 Lenina street, RU'
        print('Сообщение верно!')

        """Удаление новой локации"""
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id":place_id

        }

        result_delete = requests.delete(delete_url, json = json_for_delete_new_location)
        print(result_delete.text)
        print(result_delete.status_code)
        result_delete_status = result_delete.json()
        info_result_delete_status = result_delete_status.get('status')
        print(f'Статус: {info_result_delete_status}')
        assert info_result_delete_status == 'OK'
        print('Удалена новая локация!')

        '''Проверяем удалилась ли локация'''
        result_get = requests.get(get_url)
        print(result_get.text)
        print(f"Статус код: {result_get.status_code}")
        assert 404 == result_get.status_code
        print('Проверка удаления локации прошла успешно!')
        check_delete = result_get.json()
        check_delete_info = check_delete.get('msg')
        assert check_delete_info == "Get operation failed, looks like place_id  doesn't exists"
        print('Локация не обнаружена!')

        print('Тестирование Test_new_locathion - завершено!')

new_place = Test_new_locathion()
new_place.test_create_new_locathion()