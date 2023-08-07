from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from dependencies import get_jinja_environment

router = APIRouter(prefix='')


@router.get('/', response_class=HTMLResponse)
async def get_index(
        request: Request,
        jinja_environment: Jinja2Templates = Depends(get_jinja_environment)
):

    dados = [
        {
            'moeda':'BTC',
            'segunda': 150000.00,
            'terca': 150000.00,
            'quarta': 150000.00,
            'quinta': 150000.00,
            'sexta': 150000.00,
            'sabado': 150000.00,
         },

        {
            'moeda': 'dolar',
            'segunda': 150000.00,
            'terca': 150000.00,
            'quarta': 150000.00,
            'quinta': 150000.00,
            'sexta': 150000.00,
            'sabado': 150000.00,
        },

    ]

    return jinja_environment.TemplateResponse(
        'index.html',
        {'request': request, 'dados':dados}
    )
