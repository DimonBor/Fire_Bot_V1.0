import requests
def call_service(number): 
    params = (
        ('hcode', 'b5f7ac4514f7c0a1133fb71ffcc99f1b'),
        ('phone', number),
    )
    response = requests.get('https://my.citrus.ua/hunter/', params=params)
