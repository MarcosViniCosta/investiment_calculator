from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from dependencies import get_jinja_environment, get_price_quote_gateways
from domain.gateway.price_quote import PriceQuoteGateway

router = APIRouter(prefix='')


@router.get('/', response_class=HTMLResponse)
async def get_index(
        request: Request,
        jinja_environment: Jinja2Templates = Depends(get_jinja_environment),
        price_quote_gateways: List[PriceQuoteGateway] = Depends(get_price_quote_gateways)

):
    bit_preco = price_quote_gateways[0]

    value = await bit_preco.get_price('BTC')
    dados = list([dict(currency='BTC', bit_preco=value)])

    return jinja_environment.TemplateResponse(
        'index.html',
        {'request': request, 'dados': dados}
    )
