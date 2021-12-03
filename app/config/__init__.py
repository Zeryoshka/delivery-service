import os
from app.config.cli_parser import api_parser
from app.config import default

NAMES_OF_VARS = [
    'PORT',
    'DB_PORT',
    'DB_HOST',
    'DB_USER',
    'DB_PASSWORD',
    'DB_NAME'
]


class Config:
    def _get_env_vars(self) -> None:
        for var_name in NAMES_OF_VARS:
            if not getattr(self, var_name):
                default_value = getattr(default, 'DEFAULT_' + var_name)
                value = os.environ.get(var_name, default_value)
                setattr(self, var_name, value)

    def _get_cli_vars(self) -> None:
        cli_args = vars(api_parser.parse_args())
        for key, value in cli_args.items():
            config_value = value[0] if value else None
            setattr(self, key, config_value)

    def __init__(self) -> None:
        self._get_cli_vars()
        self._get_env_vars()
