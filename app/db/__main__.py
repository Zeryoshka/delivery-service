import os
from alembic.config import CommandLine, Config

from app.config.default import DEFAULT_DB_HOST, \
    DEFAULT_DB_USER, DEFAULT_DB_PASSWORD, \
    DEFAULT_DB_NAME, DEFAULT_DB_PORT


def main():
    alembic = CommandLine()

    alembic.parser.add_argument(
        '--db-host', type=str, default=os.getenv('DB_HOST', DEFAULT_DB_HOST)
    )
    alembic.parser.add_argument(
        '--db-port', type=int, default=os.getenv('DB_PORT', DEFAULT_DB_PORT)
    )
    alembic.parser.add_argument(
        '--db-password', type=str, default=os.getenv('DB_PASSWORD', DEFAULT_DB_PASSWORD),
    )
    alembic.parser.add_argument(
        '--db-user', type=str, default=os.getenv('DB_USER', DEFAULT_DB_USER)
    )
    alembic.parser.add_argument(
        '--db-name', type=str, default=os.getenv('DB_NAME', DEFAULT_DB_NAME)
    )
    options = alembic.parser.parse_args()

    options.config = os.path.join('app', options.config)
    config = Config(
        file_=options.config,
        ini_section=options.name,
        cmd_opts=options
    )

    config.set_main_option(
        'sqlalchemy.url',
        f'postgresql+psycopg2://{options.db_user}:{options.db_password}@{options.db_host}:{options.db_port}/{options.db_name}'
    )
    exit(alembic.run_cmd(config, options))


if __name__ == '__main__':
    main()
