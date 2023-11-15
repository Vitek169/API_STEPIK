import requests

url ='https://api.chucknorris.io/jokes/random'
print(url)
result = requests.get(url)
print(f'Status cod: {result.status_code}')
assert 200 == result.status_code
print('Good test!!!')
result.encoding = 'utf-8'
print(result.text)
