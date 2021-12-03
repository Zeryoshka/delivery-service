import logging
from typing import Callable
from aiohttp import web

from app.api.handlers import handlers
from app.api.middlewares import middlewares
from app.db import DB
from app.config import Config

logger = logging.getLogger(__name__)

def create_startup_function(config: Config) -> Callable:
    async def on_start(app: web.Application) -> None:
        app['db'] = DB(config)
        app['config'] = config
        logger.info('App started')

    return on_start


def create_app(config: Config) -> web.Application:
    app = web.Application(middlewares=middlewares)

    for handler in handlers:
        app.router.add_route('*', handler.URL, handler)

    on_start = create_startup_function(config)
    app.on_startup.append(on_start)

    return app
