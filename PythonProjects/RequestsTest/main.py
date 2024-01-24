"""
Создание покемона
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
header = {
    'Content-Type': 'application/json',
    'trainer_token': '5f0325abe73bd345a335fe30efa9441b'
}
body = {
    'name': 'Piplup2',
    'photo': 'https://dolnikov.ru/pokemons/albums/020.png' 
}
response = requests.post(url=f'{URL}/pokemons', json=body, headers = header )
print (f'Статус код :{response.status_code}. Сообщение : {response.text}')

"""
Изменение имени
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
header = {
    'Content-Type': 'application/json',
    'trainer_token': '5f0325abe73bd345a335fe30efa9441b'
}
body = {
    'pokemon_id': '28133',
    'name': 'NewPip'  
}
response = requests.patch(url=f'{URL}/pokemons', json=body, headers = header )
print (f'Статус код :{response.status_code}. Сообщение : {response.text}')

"""
Поймать покемона в покебол
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
header = {
    'Content-Type': 'application/json',
    'trainer_token': '5f0325abe73bd345a335fe30efa9441b'
}
body = {
    'pokemon_id': '28134'  
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers = header )
print (f'Статус код :{response.status_code}. Сообщение : {response.text}')