from abc import ABCMeta, abstractmethod


class PriceQuoteGateway(metaclass=ABCMeta):

    @abstractmethod
    async def get_price(self, currency: str) -> float:
        ...
