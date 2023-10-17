
import asyncio
from revolut import Client, Environment, Order, OrderModel, Currency
from typing import Optional
from os import getenv

API_KEY = getenv("API_KEY")

test_order_created: Optional[OrderModel] = None

CLIENT = Client(secret_key=API_KEY, environment=Environment.SANDBOX)
ORDER_CLIENT = Order(CLIENT)

LOOP = asyncio.get_event_loop()


def test_order_create():
    new_order = OrderModel(amount=100, currency=Currency.DKK, description="Test description of this order.")
    order_created = ORDER_CLIENT.create(new_order)

    assert order_created.id is not None
    global test_order_created
    test_order_created = order_created


def test_order_create_async():
    new_order = OrderModel(amount=100, currency=Currency.DKK, description="Test description of this order.")
    order_created = LOOP.run_until_complete(ORDER_CLIENT.create_async(new_order))

    assert order_created.id is not None


def test_order_get():
    order = ORDER_CLIENT.get(test_order_created.id)
    assert order.checkout_url == test_order_created.checkout_url


def test_order_get_async():
    order = LOOP.run_until_complete(ORDER_CLIENT.get_async(test_order_created.id))
    assert order.checkout_url == test_order_created.checkout_url


def test_order_get_list():
    orders = ORDER_CLIENT.get_list()
    assert len(orders) > 1

def test_order_get_list_async():
    orders = LOOP.run_until_complete(ORDER_CLIENT.get_list_async())
    assert len(orders) > 1


def test_order_update():
    pass
