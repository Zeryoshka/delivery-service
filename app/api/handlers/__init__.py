from app.api.handlers.delivery import DeliveryPriceView
from app.api.handlers.dishes import DishesView, OneDishView
from app.api.handlers.ping import PingView, PingDBView
from app.api.handlers.orders import OrdersView, OneOrderView, OrderStatusView

handlers = [
    PingView,
    PingDBView,
    OrdersView,
    OneOrderView,
    OrderStatusView,
    DeliveryPriceView,
    DishesView,
    OneDishView
]
