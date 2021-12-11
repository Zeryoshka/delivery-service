from app.api.handlers.ping import PingView, PingDBView
from app.api.handlers.dishes import OrderView

handlers = [
    PingView,
    PingDBView,
    OrderView
]
