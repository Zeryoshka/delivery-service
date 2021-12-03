from typing import Callable
from aiohttp import web

from app.api.handlers import handlers
from app.db import DB
from app.config import Config


def create_startup_function(config: Config) -> Callable:
    async def on_start(app: web.Application) -> None:
        app['db'] = DB(config)
        app['config'] = config

    return on_start


def create_app(config: Config) -> web.Application:
    app = web.Application()

    for handler in handlers:
        app.router.add_route('*', handler.URL, handler)

    on_start = create_startup_function(config)
    app.on_startup.append(on_start)

    return app
