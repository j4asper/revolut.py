from .client import Client
from .models import OrderModel, State
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
            response = session.post(url=self._client._base_url + "orders", data=order.model_dump_json(exclude_unset=True))

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
            response = await session.post(url=self._client._base_url + "orders", data=order.model_dump_json(exclude_unset=True))
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
        """https://developer.revolut.com/docs/merchant/update-order"""
        pass

    async def update_async(self, order_id: str, updated_order: OrderModel) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/update-order"""
        pass

    def get_list(self,
                 created_before: Optional[datetime],
                 from_created_date: Optional[datetime],
                 to_created_date: Optional[datetime],
                 customer_id: Optional[str],
                 email: Optional[str],
                 merchant_order_ext_ref: Optional[str],
                 state: Optional[State],
                 limit=100
                 ) -> list[OrderModel]:
        """https://developer.revolut.com/docs/merchant/retrieve-order-list"""
        pass

    async def get_list_async(self,
                             created_before: Optional[datetime],
                             from_created_date: Optional[datetime],
                             to_created_date: Optional[datetime],
                             customer_id: Optional[str],
                             email: Optional[str],
                             merchant_order_ext_ref: Optional[str],
                             state: Optional[State],
                             limit=100
                             ) -> list[OrderModel]:
        """https://developer.revolut.com/docs/merchant/retrieve-order-list"""
        pass

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
