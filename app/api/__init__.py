from aiohttp import web

from app.api.handlers import handlers
from app.db import DB

async def on_start(app: web.Application) -> None:
    app['db'] = DB()



def create_app() -> web.Application:
    app = web.Application()

    for handler in handlers:
        app.router.add_route('*', handler.URL, handler)
    app.on_startup.append(on_start)

    return app
