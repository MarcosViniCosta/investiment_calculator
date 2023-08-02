from fastapi import FastAPI
from uvicorn import run

from controller.ui.index import router


if __name__ == '__main__':
    app = FastAPI()
    app.include_router(router)

    run(app=app, host='0.0.0.0', port=8080)