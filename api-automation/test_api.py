# Корнеев Леонид, 40-я когорта — Финальный проект. Инженер по тестированию плюс
import requests


# ────────────────────────────────────────────────
#                 БАЗОВЫЙ URL
# ────────────────────────────────────────────────

BASE_URL = "https://540db4d3-d82d-43dc-9134-746bf5a6fc2f.serverhub.praktikum-services.ru"


# ────────────────────────────────────────────────
#               ДАННЫЕ ДЛЯ ТЕСТА
# ────────────────────────────────────────────────

def get_test_order_data():
    return {
        "firstName": "Тест",
        "lastName": "Автотест",
        "address": "ул. Тестовая, 10",
        "metroStation": "15",
        "phone": "+79998887766",
        "rentTime": 3,
        "deliveryDate": "2026-04-20",
        "comment": "Проверка API",
        "color": ["BLACK"]
    }


# ────────────────────────────────────────────────
#          ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ API
# ────────────────────────────────────────────────

def create_order():
    payload = get_test_order_data()
    
    response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=payload
    )
    response.raise_for_status()
    
    return response.json()["track"]


def get_order_by_track(track):
    response = requests.get(
        f"{BASE_URL}/api/v1/orders/track?t={track}"
    )
    response.raise_for_status()
    
    return response.json()


# ────────────────────────────────────────────────
#                   ТЕСТ
# ────────────────────────────────────────────────

def run_test_create_and_get_order():
    try:
        track = create_order()
        
        order_data = get_order_by_track(track)
        
        
        received_track = order_data.get("order", {}).get("track")
        
        if received_track == track:
            print("Тест пройден")
            return True
        else:
            print(f"Тест НЕ пройден: трек не совпал (получен {received_track}, ожидался {track})")
            return False
            
    except Exception as e:
        print(f"Тест НЕ пройден: ошибка при выполнении → {e}")
        return False


# ────────────────────────────────────────────────
#                   ЗАПУСК
# ────────────────────────────────────────────────

if __name__ == "__main__":
    run_test_create_and_get_order()