from os.path import join, dirname, realpath

from fastapi.templating import Jinja2Templates

from infra.price_quote.bit_preco import PriceQuoteBitPrecoGateway

_JINJA_ENV = None


async def get_jinja_environment():
    global _JINJA_ENV
    if not _JINJA_ENV:
        dir_templates = join(dirname(realpath(__file__)), 'templates')
        _JINJA_ENV = Jinja2Templates(dir_templates)
    return _JINJA_ENV


async def get_price_quote_gateways():
    return [PriceQuoteBitPrecoGateway()]
