import requests
import json


url = "http://127.0.0.1:8000/get_form/"
params = {
    1: {"order_date": "2023-02-30", # запрос с невалидными данными
        "customer_email": "email@com",
        "customer_phone": "+7 123 456 78",
        "description": "text"},
    2: {"order_date": "2023-11-19", # запрос с валидными данными
        "customer_email": "email@email.ru",
        "customer_phone": "+7 123 456 78 90",
        "description": "text",
        "field": "field"},
    3: {},                          # пустой запрос
    4: {"in_date": "2023-11-20",    # валидный запрос с разным форматом дат
        "out_date": "25.11.2023",
        "client_email": "email@email.ru",
        "client_phone": "+7 123 456 78 90",
        "description": "text"},
}
json_response = {
    1: {"order_date":"text",
        "customer_email": "text",
        "customer_phone": "text",
        "description": "text"},
    2: {"name": "Order"},
    3: {},
    4: {"name": "Rezervation"},
}
for k, v in params.items():
    response = requests.post(url=url, params=v)
    assert response.text == json.dumps(json_response[k])
print('ok')
