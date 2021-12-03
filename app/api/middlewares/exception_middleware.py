import logging
from typing import Callable
from http import HTTPStatus

from aiohttp import web

logger = logging.getLogger(__name__)

@web.middleware
async def exception_middleware(request: web.Request, handler: Callable) -> web.Response:
    try:
        return await handler(request)
    except web.HTTPError as err:
        logger.info(f'Caught exception (status {err.status_code})')
        return web.json_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
    except Exception as err:
        logger.error(f'Uncaught exception (status 500): {err}')
        return web.json_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
