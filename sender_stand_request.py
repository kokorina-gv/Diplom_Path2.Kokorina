import configuration
import requests
import data


# Создание заказа
def post_create_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


order_track = str(post_create_orders(data.orders_body).json()['track'])


# Получение информации по его номеру
def get_orders_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK + str(track))


response = get_orders_track(order_track)
