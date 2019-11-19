import requests
import time
def sms_service(number):
    headers = {
        'content-type': 'application/json',
        'x-app-token': 'yF27jwg5orUVo4abrops',
    }

    data = '{"identity": "'+number+'"}'

    response = requests.post('https://my.citrus.ua/api/auth/login', headers=headers, data=data)