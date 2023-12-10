# Галина Кокорина, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


# Функция проверки создания заказа
def positive_assert_create_order(body):
    create_response = sender_stand_request.post_create_orders(body)
    assert create_response.status_code == 201
    assert create_response.json() != ""


# Функция проверки получения заказа по треку заказа
def positive_assert_get_order_by_track(track):
    track_response = sender_stand_request.get_orders_track(track)
    assert track_response.status_code == 200
    assert track_response.json() != ""


def test_order_create():
    positive_assert_create_order(data.orders_body)
def test_get_order_by_track():
    positive_assert_get_order_by_track(sender_stand_request.order_track)
