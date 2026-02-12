# Корнеев Леонид, 40-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

BASE_URL = "https://b4f6d486-3dcc-496d-940a-01110f32b65f.serverhub.praktikum-services.ru"

def create_order():
    payload = {
        "firstName": "Test",
        "lastName": "User",
        "address": "ул. Тестовая 1",
        "metroStation": "1",
        "phone": "+79999999999",
        "rentTime": 1,
        "deliveryDate": "2026-02-05",
        "comment": "Тестовый комментарий",
        "color": ["BLACK"]
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=payload)
    response.raise_for_status()
    return response.json()["track"]

def get_order_by_track(track):
    response = requests.get(f"{BASE_URL}/api/v1/orders/track?t={track}")
    response.raise_for_status()
    return response.status_code, response.json()

def test_create_and_get_order():
    print("Шаг 1: Создаём заказ...")
    track = create_order()
    print(f"Создан заказ с треком: {track}")
    
    print("Шаг 2: Получаем заказ по треку...")
    status_code, data = get_order_by_track(track)
    
    assert status_code == 200, f"Ожидали 200, получили {status_code}"
    print("Тест пройден: заказ успешно получен по треку")
    print(f"Данные заказа: {data}")

if __name__ == "__main__":
    test_create_and_get_order()