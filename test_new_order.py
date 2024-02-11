# Антонов Николай, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
track = post_create_new_order(data.create_order_body).json()["track"]

def get_order_number(number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER + str(number))
response = get_order_number(track)

def test_get_order_get_success_response():
    response = post_create_new_order(data.create_order_body)
    track = response.json()["track"]
    get_order = get_order_number(track)
    assert get_order.status_code == 200