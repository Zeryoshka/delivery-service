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

api_parser.add_argument('--LOG_FILE', dest='LOG_FILE', type=str, nargs=1, default=None)
api_parser.add_argument('--LOG_LEVEL', dest='LOG_LEVEL', type=str, nargs=1, default=None)
