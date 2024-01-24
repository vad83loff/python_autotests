import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
header = {
    'Content-Type': 'application/json',
}
''' проверка на имя тренера'''
def test_get_trainers():
    response = requests.get(url=f'{URL}/trainers',params= {'trainer_id': 3690}, timeout=5 )
    assert response.json()['trainer_name'] == 'Vadim'


''' проверка на статус код'''
def test_get_trainers_by_id():
    response = requests.get(url=f'{URL}/trainers', timeout=5 )
    assert response.status_code == 200,'Неправильный статус код'
