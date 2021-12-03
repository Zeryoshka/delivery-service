# Delivery-service

## Installing
Install package with dev dependencies
```bash
pip insall -e .[dev]
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

## Logging
We create logging to delivery-service. By default service writes logs to stdout, but if you set LOG_FILE variable, you can write logs to files.
If you want to decrease verbosity, you can set LOG_LEVEL variable to WARN or ERROR (By default LOG_LEVEL=INFO).