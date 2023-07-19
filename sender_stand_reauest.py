import config
import requests
import data


def create_new_order(body):
    response=requests.post(config.URL+config.CREATE_ORDER_API,
                           json=body)
    return response.json()["track"]

def get_order(): 
    order = requests.get(config.URL+config.GET_ORDER_API, params={"t": create_new_order(data.body_create)})
    return order
