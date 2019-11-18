import requests


def call_service(number):
        
    headers = {
        'authority': 'my.citrus.ua',
        'x-locale': 'ru',
        'origin': 'https://www.citrus.ua',
        'x-device-type': 'desktop',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'accept': 'application/json, text/plain, */*',
        'x-auth-token': 'K5GDpMMPGCWgmfhu',
        'user-token': 'K5GDpMMPGCWgmfhu',
        'x-app-token': 'yF27jwg5orUVo4abrops',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://www.citrus.ua/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
    }

    params = (
        ('hcode', 'b5f7ac4514f7c0a1133fb71ffcc99f1b'),
        ('phone', number),
    )

    response = requests.get('https://my.citrus.ua/hunter/', headers=headers, params=params)
