# Корнеев Леонид, 40-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_order_and_get_by_track_success():
    response_create = sender_stand_request.post_new_order()
    
    track = response_create.json()["track"]
    
    response_get = sender_stand_request.get_order_by_track(track)
    order_data = response_get.json()
    
    received_track = order_data["order"]["track"]
    assert received_track == track, \
        f"Трек-номера не совпали: ожидался {track}, получен {received_track}"