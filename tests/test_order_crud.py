
import asyncio
from revolut import Client, Environment, Order, OrderModel, Currency
from os import getenv

API_KEY = getenv("API_KEY")

test_order_id = None
test_order_created = None


def test_order_create():
    client = Client(secret_key=API_KEY, environment=Environment.SANDBOX)
    order = Order(client)
    new_order = OrderModel(amount=100, currency=Currency.DKK, description="Test description of this order.")
    order_created = order.create(new_order)

    assert order_created.id is not None
    global test_order_id
    global test_order_created
    test_order_id = order_created.id
    test_order_created = order_created


def test_order_create_async():
    client = Client(secret_key=API_KEY, environment=Environment.SANDBOX)
    order = Order(client)
    new_order = OrderModel(amount=100, currency=Currency.DKK, description="Test description of this order.")
    loop = asyncio.get_event_loop()
    order_created = loop.run_until_complete(order.create_async(new_order))

    assert order_created.id is not None


def test_order_get():
    pass


def test_order_update():
    pass


def test_order_get_list():
    pass

