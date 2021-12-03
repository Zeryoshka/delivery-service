from aiohttp import web

from app.api import create_app
from app.config import Config

def main():
    config = Config()
    app = create_app()
    web.run_app(app, host='0.0.0.0', port=config.PORT)
