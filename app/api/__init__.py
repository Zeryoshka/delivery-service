from aiohttp import web

from app.api.handlers import handlers


def create_app() -> web.Application:
    app = web.Application()
    for handler in handlers:
        app.router.add_route('*', handler.URL, handler)
    return app
