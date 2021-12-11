class GeoServiceError(Exception):
    pass

class RouteNotFound(GeoServiceError):
    pass

class GeoApiError(GeoServiceError):
    pass