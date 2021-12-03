from aiohttp import web

from app.db import DB

class BaseView(web.View):

    @property
    def db(self) -> DB:
        return self.request.app['db']
