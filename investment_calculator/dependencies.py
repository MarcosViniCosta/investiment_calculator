import sys
from os.path import join, dirname, realpath
from typing import List

from fastapi.templating import Jinja2Templates
import inspect
from infra.gateway.price_quote import *

from domain.gateway.price_quote import PriceQuoteGateway

_JINJA_ENV = None


async def get_jinja_environment():
    global _JINJA_ENV
    if not _JINJA_ENV:
        dir_templates = join(dirname(realpath(__file__)), 'templates')
        _JINJA_ENV = Jinja2Templates(dir_templates)
    return _JINJA_ENV


async def get_price_quote_gateways() -> List[PriceQuoteGateway]:
    result = []
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and issubclass(obj, PriceQuoteGateway) and obj != PriceQuoteGateway:
            result.append(obj())
    return result
