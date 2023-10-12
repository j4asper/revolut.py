from .client import Client
from .models import Currency, OrderModel, State
from typing import Optional
from datetime import datetime


class Order:
    def __init__(self, client: Client):
        self._client = client

    def create(self, amount: int, currency: Currency) -> OrderModel:
        """https://developer.revolut.com/docs/merchant/create-order"""
        pass

    async def create_async(self, amount: int, currency: Currency) -> OrderModel:
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
