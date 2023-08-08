from domain.gateway.price_quote import PriceQuoteGateway


class PriceQuoteBitPrecoGateway(PriceQuoteGateway):
    async def get_price(self, currency: str) -> float:
        return 142_906.000001