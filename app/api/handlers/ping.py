from http import HTTPStatus
from aiohttp import web

from app.api.handlers.base_view import BaseView


class PingView(web.View):
    URL = r'/ping'

    async def get(self) -> web.Response:
        return web.json_response(status=HTTPStatus.OK)

class PingDBView(BaseView):
    URL = r'/ping_db'

    async def get(self) -> web.Response:
        await self.db.ping()
        return web.json_response(status=HTTPStatus.OK)
