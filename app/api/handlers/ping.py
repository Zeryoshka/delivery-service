from http import HTTPStatus

from aiohttp import web


class PingView(web.View):
    URL = r'/ping'

    async def get(request: web.Request) -> web.Response:
        return web.json_response(status=HTTPStatus.OK)
