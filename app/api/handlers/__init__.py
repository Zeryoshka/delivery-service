from app.api.handlers.ping import PingView, PingDBView
from app.api.handlers.orders import OrdersView, OneOrderView, OrderStatusView

handlers = [
    PingView,
    PingDBView,
    OrdersView,
    OneOrderView,
    OrderStatusView,
]
