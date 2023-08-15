from aiohttp import ClientSession

from domain.gateway.price_quote import PriceQuoteGateway


class PriceQuoteAwesomeApiGateway(PriceQuoteGateway):


    def __init__(self):
        self. _client = ClientSession(base_url='https://economia.awesomeapi.com.br/')
        self._table = {'BTC': 'BTC-BRL', 'ETH': 'ETH-BRL'}


    async def get_price(self, currency: str) -> float:
        market = self._table.get(currency)
        async with self._client.get(f'/last/{market}') as response:
            data = await response.json()
            pair_name = ''.join(market.split('-'))
            return data[pair_name]['bid']

    async def get_broker(self) -> str:
        return 'awesome_api'


