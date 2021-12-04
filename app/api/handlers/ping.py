import logging
from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView

logger = logging.getLogger(__name__)

class PingView(web.View):
    URL = r'/ping'

    async def get(self) -> web.Response:
        logger.info('ping service')
        return web.json_response(status=HTTPStatus.OK)

class PingDBView(BaseView):
    URL = r'/ping_db'

    async def get(self) -> web.Response:
        logger.info('ping db')
        await self.db.ping()
        return web.json_response(status=HTTPStatus.OK)
