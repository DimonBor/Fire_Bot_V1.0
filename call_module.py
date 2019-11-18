import requests
import types
@types.coroutine
def call_service(number): 
    headers = {
        'x-app-token': 'yF27jwg5orUVo4abrops',
    }
    params = (
        ('hcode', 'b5f7ac4514f7c0a1133fb71ffcc99f1b'),
        ('phone', number),
    )
    response = requests.get('https://my.citrus.ua/hunter/', headers=headers, params=params)
