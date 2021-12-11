from aiohttp import web

from app.db import DB
from app.config import Config
from app.geo_service import GeoService

class BaseView(web.View):

    @property
    def db(self) -> DB:
        return self.request.app['db']

    @property
    def config(self) -> Config:
        return self.request.app['config']

    @property
    def geo_service(self) -> GeoService:
        return self.request.app['geo_service']
