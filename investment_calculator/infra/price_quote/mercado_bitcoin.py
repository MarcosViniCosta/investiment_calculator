from aiohttp import ClientSession

from domain.gateway.price_quote import PriceQuoteGateway


class PriceQuoteMercadoBitcoinGateway(PriceQuoteGateway):

    def __init__(self):
        self._client = ClientSession(base_url='https://api.mercadobitcoin.net/')
        self._table = {'BTC': 'BTC-BRL', 'ETH': 'ETH-BRL'}

    async def get_price(self, currency: str) -> float:
        market = self._table.get(currency)
        symbols = {'symbols': market}
        async with self._client.get(f'/api/v4/tickers', params=symbols) as response:
            data = await response.json()
            return data[0]['sell']

    async def get_broker(self) -> str:
        return 'mercado_bitcoin'



