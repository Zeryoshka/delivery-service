
import logging
from typing import Callable

from aiohttp import web

logger = logging.getLogger(__name__)

@web.middleware
async def rps_limiter_middleware(request: web.Request, handler: Callable) -> web.Response:
    if await request.app['rps_limiter'].is_limit(request.rel_url):
        logger.info(f'User get 429 status code on {request.rel_url}')
        raise web.HTTPTooManyRequests()
    return await handler(request)
