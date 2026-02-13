import requests
import configuration
import data


def post_new_order():
    """Создание нового заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=data.order_body,
        headers=data.headers
    )


def get_order_by_track(track):
    """Получение заказа по трек-номеру"""
    params = {"t": track}
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        params=params,
        headers=data.headers
    )