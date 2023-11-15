import requests

class NewJoke:
    """"New joke creation"""

    def __init__(self):
        pass
    """ММетод создания новой шутки рандомной"""
    # def create_new_random_joke_test(self):
    #     """Random joke creation"""
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print("Status code " + str(result.status_code))
    #     assert 200 == result.status_code
    #     print("Success! We got new joke ")
    #     print(result.text)
    #     check = result.json()
    #     # check_info = check.get('categories')
    #     # print(check_info)
    #     # assert check_info == []
    #     # print('Good Test')
    #     check_info_value = check.get('value')
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print('Yes')
    #     else:
    #         print('No')

    """Метод создания шутки по категории"""
    def create_new_categories_joke_test(self):
        """Random joke creation"""
        category = 'sex'
        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        print(url)
        result = requests.get(url)
        print("Status code " + str(result.status_code))
        assert 404 == result.status_code
        if result.status_code == 404:
            print("This is category is not! ")
        else:
            print('Good')
        print(result.text)
        check = result.json()
        check_info = check.get('categories')
        print(check_info)
        assert check_info == ["sport"]
        print('Good Test')
        # check_info_value = check.get('value')
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print('Yes')
        # else:
        #     print('No')



# random_joke_test = NewJoke()
# random_joke_test.create_new_random_joke_test()

sport_joke =NewJoke()
sport_joke.create_new_categories_joke_test()



