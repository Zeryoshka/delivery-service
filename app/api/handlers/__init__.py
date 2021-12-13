from app.api.handlers.delivery import DeliveryPriceView
from app.api.handlers.orders import OrdersView
from app.api.handlers.ping import PingView, PingDBView
from app.api.handlers.dishes import DishView
from app.api.handlers.restaurants import RestaurantView

handlers = [
    PingView,
    PingDBView,
    DishView,
    RestaurantView,
    DeliveryPriceView,
    OrdersView
]
