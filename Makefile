start-db:
	docker run --rm -d -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=pass -e POSTGRES_DB=db -p 5432:5432 postgres
