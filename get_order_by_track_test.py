import sender_stand_request


def test_get_order_by_track(): # Проверка что код ответа равен 200
    response_code = sender_stand_request.get_order().status_code
    assert response_code == 200

    # Малинин Михаил, 6-я когорта — Финальный проект. Инженер по тестированию плюс
