from aiohttp import web

from app.db import DB
from app.config import Config

class BaseView(web.View):

    @property
    def db(self) -> DB:
        return self.request.app['db']

    @property
    def config(self) -> Config:
        return self.request.app['config']
