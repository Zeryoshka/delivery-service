from app.api.handlers.delivery import DeliveryPriceView
from app.api.handlers.ping import PingView, PingDBView

handlers = [
    PingView,
    PingDBView,
    DeliveryPriceView,
]
