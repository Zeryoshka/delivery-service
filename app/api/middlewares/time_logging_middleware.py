import logging
from typing import Callable
from time import time

from aiohttp import web

logger = logging.getLogger(__name__)

@web.middleware
async def time_logging_middleware(request: web.Request, handler: Callable) -> web.Response:
    logger.info(f'Start {request.method} {request.url} request')
    start = time()
    response = await handler(request)

    finish = time()
    logger.info(f'Finished {request.method} {request.url} request for {(finish - start) * 1000}ms')
    return response
