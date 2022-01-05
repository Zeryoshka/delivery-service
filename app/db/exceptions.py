class DatabaseClientError(Exception):
    """
    Base class for all database exceptions
    """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class DishDatabaseError(DatabaseClientError):
    """
    Base class for all dish methods errors
    """
    def __init__(self, args=None, message='Default message') -> None:
        self.args = args
        self.message = message
        super().__init__(self.message)


class RestaurantDatabaseError(DatabaseClientError):
    """
    Base class for all restaurant methods errors
    """
    def __init__(self, args=None, message='Default message') -> None:
        self.args = args
        self.message = message
        super().__init__(self.message)


class OrderDatabaseError(DatabaseClientError):
    """
    Base class for all order methods errors
    """
    def __init__(self, message='Default message') -> None:
        self.message = message
        super().__init__(self.message)
