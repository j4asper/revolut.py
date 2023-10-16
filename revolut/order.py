from .client import Client
from .models import OrderModel, State
from typing import Optional
from datetime import datetime
from requests import Session


class Order:
    def __init__(self, client: Client):
        self._client = client
        self._base_url = client._base_url + "orders"

    def create(self, order: OrderModel) -> OrderModel:
        """
        amount and currency fields in the OrderModel are required.

        https://developer.revolut.com/docs/merchant/create-order
        """
        if not order.amount or not order.currency:
            raise AttributeError("OrderModel missing attributes Amount and/or Currency")

        with Session() as session:
            session.headers = self._client._headers
            response = session.post(url=self._base_url, data=order.model_dump_json(exclude_unset=True))

        if response.status_code == 201:
            return OrderModel(**response.json())
        elif response.status_code == 401:
            raise Exception("Invalid API Key provided")



    async def create_async(self, order: OrderModel) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/create-order"""
        pass

    def get(self, order_id: str) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/retrieve-order"""
        pass

    async def get_async(self, order_id: str) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/retrieve-order"""
        pass

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
