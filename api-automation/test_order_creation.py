# Корнеев Леонид, 40-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_create_order_and_get_by_track_success():
    response_create = sender_stand_request.post_new_order()
    
    assert response_create.status_code == 201, \
        f"Ожидался статус 201, получен {response_create.status_code}"
    
    track = response_create.json().get("track")
    assert track is not None, "В ответе отсутствует поле track"
    assert isinstance(track, int), "track должен быть целым числом"
    
    response_get = sender_stand_request.get_order_by_track(track)
    
    assert response_get.status_code == 200, \
        f"Ожидался статус 200, получен {response_get.status_code}"
    
    order_data = response_get.json()
    
    assert "order" in order_data, "В ответе отсутствует ключ 'order'"
    
    received_track = order_data["order"].get("track")
    assert received_track == track, \
        f"Трек-номера не совпали: ожидался {track}, получен {received_track}"