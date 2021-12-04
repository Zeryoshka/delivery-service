from app.api.middlewares.exception_middleware import exception_middleware
from app.api.middlewares.time_logging_middleware import time_logging_middleware
from app.api.middlewares.rps_limiter_middleware import rps_limiter_middleware

middlewares = [
    time_logging_middleware,
    exception_middleware,
    rps_limiter_middleware,
]
