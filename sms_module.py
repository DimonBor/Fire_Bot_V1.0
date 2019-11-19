import requests
import time
import types
def sms_service(number):
    headers = {
        'x-app-token': 'yF27jwg5orUVo4abrops',
    }

    data = { 'identity': number}

    response = requests.post('https://my.citrus.ua/api/auth/login', headers=headers, json=data)