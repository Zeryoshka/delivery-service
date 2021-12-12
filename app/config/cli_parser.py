from argparse import ArgumentParser

api_parser = ArgumentParser(description='''
    Start delivery-api service
    You can use ENV VARIABLES or CLI flags to set parametres
''')

api_parser.add_argument('--DB_PORT', dest='DB_PORT', type=int, nargs=1, default=None)
api_parser.add_argument('--DB_HOST', dest='DB_HOST', type=str, nargs=1, default=None)
api_parser.add_argument('--DB_USER', dest='DB_USER', type=str, nargs=1, default=None)
api_parser.add_argument('--DB_PASSWORD', dest='DB_PASSWORD', type=str, nargs=1, default=None)
api_parser.add_argument('--DB_NAME', dest='DB_NAME', type=str, nargs=1, default=None)

api_parser.add_argument('--PORT', dest='PORT', type=int, nargs=1, default=None)

api_parser.add_argument('--MAX_RPS', dest='MAX_RPS', type=int, nargs=1, default=None)

api_parser.add_argument('--LOG_FILE', dest='LOG_FILE', type=str, nargs=1, default=None)
api_parser.add_argument('--LOG_LEVEL', dest='LOG_LEVEL', type=str, nargs=1, default=None)

api_parser.add_argument('--API_KEY', dest='API_KEY', type=str, nargs=1, default=None)
api_parser.add_argument('--MIN_COST', dest='MIN_COST', type=int, nargs=1, default=None)
api_parser.add_argument('--MONEY_FOR_METER', dest='MONEY_FOR_METER', type=int, nargs=1, default=None)
api_parser.add_argument('--GEO_API_MODE', dest='GEO_API_MODE', type=str, nargs=1, default=None)
