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
    return jinja_environment.TemplateResponse(
        'index.html',
        {'request': request}
    )
