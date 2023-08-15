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
    dados = []
    for currency in ('BTC','ETH'):
        buffer = {'currency': currency}
        for gateway in price_quote_gateways:
            value = await gateway.get_price(currency)
            broker = await gateway.get_broker()
            buffer[broker] = value
        dados.append(buffer)



    #bit_preco = price_quote_gateways[0]
    #mercado_bitcoin = price_quote_gateways[1]
    #awesome_api = price_quote_gateways[2]
    #value_bit_preco = await bit_preco.get_price('BTC')
    #value_mercado_bitcoin = await mercado_bitcoin.get_price('BTC')
    #value_awesome_preco = await awesome_api.get_price('BTC')

    #dados = list([dict(currency='BTC', bit_preco=value_bit_preco, mercado_bitcoin=value_mercado_bitcoin, awesome_api=value_awesome_preco)])

    return jinja_environment.TemplateResponse(
        'index.html',
        {'request': request, 'dados': dados}
    )
