# Delivery-service
## Installing
Install package with dev dependencies
```bash
pip install -e .[dev]
```

Install package without dev dependencies
```bash
pip install .
```

## Testing

Testing with pytest
```bash
pytest
```

To calculate coverage
```bash
pytest --cov=app
```



## Using
For start app (after installing)

```bash
delivery-api
```

## DB
You can use `make` to start db (we set base configuring for postgres)
```bash
make start-db
```

## Configuring
You can use one of two configuring methods or combine it.
Configuring methods:
* CLI
* Environment variables
If you use CLI for configuring after environment variables system will use CLI

### Variables and default values
```
PORT = 8080

MAX_RPS = 0

LOG_FILE = None
LOG_LEVEL = INFO

DB_PORT = 5432
DB_HOST = localhost
DB_USER = postgres
DB_PASSWORD = postgres
DB_NAME = db
```


### Configuring in CLI
Example CLI flags for configuring
```bash
delivery-api --PORT 5000 --DB_PORT 5433
```

## Migrations
This service use alembic for working with migrations. Alembic - universal util for migrations connecting to sqlalchemy.
You can use `delivery-db` instead base alembic's util, with special CLI parameters to configure postgres connection (or os environments).
Default values match with default service values.
```bash
--db-host BD_HOST
--db-port DB_PORT
--db-password DB_PASSWORD
--db-user DB_USER
--db-name DB_NAME
```

### Simple usage
To revise new migration you need to start db with last revision and command
```bash
delivery-db revision --message="message" --autogenerate
```
To upgrade db to cur revision you need to use next command
```bash
delivery-db upgrade head
```

## Logging
We create logging to delivery-service. By default service writes logs to stdout, but if you set LOG_FILE variable, you can write logs to files.
If you want to decrease verbosity, you can set LOG_LEVEL variable to WARN or ERROR (By default LOG_LEVEL=INFO).

## limiting RPS
System can limit RPS. If MAX_RPS==0 then system set non limit rps. If you set limit rps, users will not use rout more then `MAX_RPS` per second (for all routes). System limiting rps thread-safe, based on `asyncio.lock`.
