from .client import Client
from .models import OrderModel, State, PartialOrderModel, OrderFilter
from typing import Optional
from datetime import datetime
from requests import Session
from aiohttp import ClientSession


class Order:
    def __init__(self, client: Client):
        self._client = client

    def _handle_order_create_data(self, status_code: int, data: dict = None):
        if status_code == 201:
            return OrderModel(**data)
        elif status_code == 400:
            raise Exception("Invalid OrderModel provided")
        elif status_code == 401:
            raise Exception("Invalid API Key provided")
        else:
            raise Exception("Unknown error occurred")

    def create(self, order: OrderModel) -> OrderModel:
        """
        amount and currency fields in the OrderModel are required.

        https://developer.revolut.com/docs/merchant/create-order
        """
        if not order.amount or not order.currency:
            raise AttributeError("OrderModel missing attributes Amount and/or Currency")

        with Session() as session:
            session.headers = self._client._headers
            response = session.post(url=self._client._base_url + "orders",
                                    data=order.model_dump_json(exclude_unset=True))

        order_model = self._handle_order_create_data(response.status_code, response.json())
        return order_model

    async def create_async(self, order: OrderModel) -> OrderModel:
        """
        amount and currency fields in the OrderModel are required.

        https://developer.revolut.com/docs/merchant/create-order
        """
        if not order.amount or not order.currency:
            raise AttributeError("OrderModel missing attributes Amount and/or Currency")

        async with ClientSession(headers=self._client._headers) as session:
            response = await session.post(url=self._client._base_url + "orders",
                                          data=order.model_dump_json(exclude_unset=True))
            json_data = await response.json()

        order_model = self._handle_order_create_data(response.status, json_data)
        return order_model

    def _handle_order_get_data(self, status_code: int, data: dict = None):
        if status_code == 200:
            return OrderModel(**data)
        elif status_code == 404:
            return None
        elif status_code == 401:
            raise Exception("Invalid API Key provided")
        else:
            raise Exception("Unknown error occurred")

    def get(self, order_id: str) -> Optional[OrderModel]:
        """https://developer.revolut.com/docs/merchant/retrieve-order"""
        with Session() as session:
            session.headers = self._client._headers
            response = session.get(url=self._client._base_url + f"orders/{order_id}")

        order_model = self._handle_order_get_data(response.status_code, response.json())
        return order_model

    async def get_async(self, order_id: str) -> Optional[OrderModel]:
        """https://developer.revolut.com/docs/merchant/retrieve-order"""
        async with ClientSession(headers=self._client._headers) as session:
            response = await session.get(url=self._client._base_url + f"orders/{order_id}")
            json_data = await response.json()

        order_model = self._handle_order_get_data(response.status, json_data)
        return order_model

    def update(self, order_id: str, updated_order: OrderModel) -> OrderModel:
        """
        You can only update certain values, if the state of an order matches the ones below. Please read the official docs below.
        https://developer.revolut.com/docs/merchant/update-order
        """
        pass

    async def update_async(self, order_id: str, updated_order: OrderModel) -> OrderModel:
        """
        You can only update certain values, if the state of an order matches the ones below. Please read the official docs below.
        https://developer.revolut.com/docs/merchant/update-order
        """
        pass

    def _handle_get_list_data(self, status_code: int, data: dict = None):
        if status_code == 200:
            orders = []
            for order in data:
                orders.append(PartialOrderModel(**order))
            return orders
        elif status_code == 404:
            return None
        elif status_code == 401:
            raise Exception("Invalid API Key provided")
        else:
            raise Exception("Unknown error occurred")

    def get_list(self,
                 created_before: Optional[datetime] = None,
                 from_created_date: Optional[datetime] = None,
                 to_created_date: Optional[datetime] = None,
                 customer_id: Optional[str] = None,
                 email: Optional[str] = None,
                 merchant_order_ext_ref: Optional[str] = None,
                 state: Optional[State] = None,
                 limit=100
                 ) -> list[PartialOrderModel]:
        """
        Get a list of orders
        https://developer.revolut.com/docs/merchant/retrieve-order-list
        """
        filter = PartialOrderModel(
            created_before=created_before,
            from_created_date=from_created_date,
            to_created_date=to_created_date,
            customer_id=customer_id,
            email=email,
            merchant_order_ext_ref=merchant_order_ext_ref,
            state=state,
            limit=limit
        )

        with Session() as session:
            session.headers = self._client._headers
            response = session.get(url=self._client._base_url + f"1.0/orders", params=filter.model_dump(exclude_none=True))

        order_list = self._handle_get_list_data(response.status_code, response.json())
        return order_list


    async def get_list_async(self,
                             created_before: Optional[datetime] = None,
                             from_created_date: Optional[datetime] = None,
                             to_created_date: Optional[datetime] = None,
                             customer_id: Optional[str] = None,
                             email: Optional[str] = None,
                             merchant_order_ext_ref: Optional[str] = None,
                             state: Optional[State] = None,
                             limit=100
                             ) -> list[PartialOrderModel]:
        """
        Get a list of orders
        https://developer.revolut.com/docs/merchant/retrieve-order-list
        """
        filter = PartialOrderModel(
            created_before=created_before,
            from_created_date=from_created_date,
            to_created_date=to_created_date,
            customer_id=customer_id,
            email=email,
            merchant_order_ext_ref=merchant_order_ext_ref,
            state=state,
            limit=limit
        )

        async with ClientSession(headers=self._client._headers) as session:
            response = await session.get(url=self._client._base_url + f"1.0/orders", params=filter.model_dump(exclude_none=True))
            json_data = await response.json()

        order_list = self._handle_get_list_data(response.status, json_data)
        return order_list

    def capture_order(self, order_id: str) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/capture-order"""
        pass

    def capture_order_async(self, order_id: str) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/capture-order"""
        pass

    def cancel(self, order_id: str) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/cancel-order"""
        pass

    def cancel_async(self, order_id: str) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/cancel-order"""
        pass

    def refund(self,
               order_id: str,
               amount: int,
               description: str = None,
               order_ext_ref: str = None,
               metadata: dict = None
               ) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/cancel-order"""
        pass

    def refund_async(self,
                     order_id: str,
                     amount: int,
                     description: str = None,
                     order_ext_ref: str = None,
                     metadata: dict = None
                     ) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/cancel-order"""
        pass
