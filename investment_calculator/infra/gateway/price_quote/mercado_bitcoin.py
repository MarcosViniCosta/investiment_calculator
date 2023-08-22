__all__ = ['PriceQuoteMercadoBitcoinModel', 'PriceQuoteMercadoBitcoinGateway']


from datetime import datetime

from aiohttp import ClientSession
from pydantic import BaseModel

from domain.gateway.price_quote import PriceQuoteGateway


class PriceQuoteMercadoBitcoinModel(BaseModel):
    pair: str
    high: float
    low: float
    vol: float
    last: float
    buy: float
    sell: float
    open: float
    date: datetime


class PriceQuoteMercadoBitcoinGateway(PriceQuoteGateway):

    def __init__(self):
        self._client = ClientSession(base_url='https://api.mercadobitcoin.net/')
        self._table = {'BTC': 'BTC-BRL', 'ETH': 'ETH-BRL'}

    async def get_price(self, currency: str) -> float:
        market = self._table.get(currency)
        symbols = {'symbols': market}
        async with self._client.get(f'/api/v4/tickers', params=symbols) as response:
            data = await response.json()
            obj_data = PriceQuoteMercadoBitcoinModel(**data[0])
            return obj_data.last

    async def get_broker(self) -> str:
        return 'mercado_bitcoin'
