from aiohttp import web

from app.api import create_app

def main():
    app = create_app()
    web.run_app(app, host='0.0.0.0', port=8080)
