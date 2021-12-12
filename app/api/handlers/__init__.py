from app.api.handlers.delivery import DeliveryPriceView
from app.api.handlers.ping import PingView, PingDBView
from app.api.handlers.dishes import OrderView
from app.api.handlers.restaurants import RestaurantView

handlers = [
    PingView,
    PingDBView,
    OrderView,
    RestaurantView
    DeliveryPriceView,
]
