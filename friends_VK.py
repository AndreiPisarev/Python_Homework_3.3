import requests
from urllib.parse import urlencode


AUTH_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6447963
VERSION = '5.74'

source_uid = 286048734  # ID пользователя, чьи друзья пересекаются с друзьями пользователя с идентификатором target_uid
target_uid = 124491235  # ID пользователя, с которым необходимо искать общих друзей.

token = '43a0837ae955fb0b72e540f121d14dd8a02501952dca6d4596c9ccc6e3e9483012f5a6d7cfe8bdb469eb0'


def authorize_vk():
    auth_data = {
        'client_id': APP_ID,
        'display': 'page',
        'response_type': 'token',
        'scope': 'friends'
    }
    print('Перейдите по ссылке для получения токена (скопируйте токен и вставте в поле ввода)')
    print('?'.join((AUTH_URL, urlencode(auth_data))))
    token1 = input('Вставьте токен:')

    return token1


def mutual_friends(source_uid, target_uid, token):
    """Для поиска общих друзей используем метод getMutual объекта friends"""

    params = {
        'v': VERSION,
        'access_token': token,
        'source_uid': source_uid,
        'target_uid': target_uid
    }

    response = requests.get('https://api.vk.com/method/friends.getMutual', params)
    response_dict = response.json()
    list_friends = response_dict['response']

    print('Список общих друзей для ID-{} и ID-{}:'.format(source_uid, target_uid))
    for friend in list_friends:
        print('https://vk.com/id{}'.format(friend))


# token = authorize_vk()
mutual_friends(source_uid, target_uid, token)


