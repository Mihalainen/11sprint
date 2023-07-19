import config
import requests
import data


def create_new_order(body): # создаю функцю получения трек-номера заказа
    response=requests.post(config.URL+config.CREATE_ORDER_API,
                           json=body)
    return response.json()["track"]

def get_order(): # создаю функцию получения кода ответа сервера при получении созданного заказа по трек-номеру
def get_order(): # создаю функцию получения ответа сервера при получении созданного заказа по трек-номеру
    order = requests.get(config.URL+config.GET_ORDER_API, params={"t": create_new_order(data.body_create)})
    return order
