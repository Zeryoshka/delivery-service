import logging
from aiohttp import web

from app.api import create_app
from app.config import Config

logger = logging.getLogger(__name__)

def main():
    config = Config()
    logging.basicConfig(
        filename=config.LOG_FILE, level=config.LOG_LEVEL,
        format='[%(asctime)s] %(name)s: (%(levelname)s) %(message)s'
    )

    app = create_app(config)
    logger.info('App created')
    web.run_app(app, host='0.0.0.0', port=config.PORT)
