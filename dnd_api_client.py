import requests

BASE_URL = 'https://www.dnd5eapi.co/api/'


def get_classes():
    response = requests.get(BASE_URL+'classes/').json()['results']
    result = list(map(lambda x: x['name'], response))
    return result