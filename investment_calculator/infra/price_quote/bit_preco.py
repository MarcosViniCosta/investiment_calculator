from aiohttp import ClientSession

from domain.gateway.price_quote import PriceQuoteGateway


class PriceQuoteBitPrecoGateway(PriceQuoteGateway):

    def __init__(self):
        self._client = ClientSession(base_url='https://api.bitpreco.com')
        self._table = {'BTC': 'btc-brl', 'ETH': 'eth-brl'}

    async def get_price(self, currency: str) -> float:
        market = self._table.get(currency)
        async with self._client.get(f'/{market}/ticker') as response:
            data = await response.json()
            return data['last']

    async def get_broker(self) -> str:
        return 'bit_preco'









