__all__ = ['PriceQuoteBitPrecoModel', 'PriceQuoteBitPrecoGateway']

from datetime import datetime

from aiohttp import ClientSession
from pydantic import BaseModel, Field

from domain.gateway.price_quote import PriceQuoteGateway

class PriceQuoteBitPrecoModel(BaseModel):
    success: bool
    market: str
    last: float
    high: float
    low: float
    vol: float
    avg: float
    var: float
    buy: float
    sell: float
    timestamp: datetime



class PriceQuoteBitPrecoGateway(PriceQuoteGateway):

    def __init__(self):
        self._client = ClientSession(base_url='https://api.bitpreco.com')
        self._table = {'BTC': 'btc-brl', 'ETH': 'eth-brl'}

    async def get_price(self, currency: str) -> float:
        market = self._table.get(currency)
        async with self._client.get(f'/{market}/ticker') as response:
            data = await response.json()
            obj_data = PriceQuoteBitPrecoModel(**data)
            return obj_data.last

    async def get_broker(self) -> str:
        return 'bit_preco'









