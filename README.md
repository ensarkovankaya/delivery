# Delivery Application

## Environment Variables

| Name          | Default   | Required | Description                                                                                     |
|---------------|-----------|:--------:|-------------------------------------------------------------------------------------------------|
| DEBUG         | false     |          | If true application will start in debug mode                                                    |
| SECRET        |           | X        | Django SECRET_KEY. This variable used for cryptography related operations like password hashing |
| ALLOWED_HOSTS | localhost |          | Comma separated list of domain names to be allowed                                              |
| DB_NAME       |           | X        | Database name                                                                                   |
| DB_USER       |           | X        | Database user                                                                                   |
| DB_PASSWORD   |           | X        | Database password                                                                               |
| DB_PORT       |           | X        | Database port                                                                                   |
| DB_HOST       |           | X        | Database host                                                                                   |

## Database Migration

After application started in background with

```shell
docker-compose up -d

# Optionally you can check if container running by following command
docker ps |grep delivery-api
```

Run below command to apply migrations

```shell
docker-compose exec api python manage.py migrate
```

## Creating Admin User

Django comes with admin interface, to access it you can go to http://localhost:8080/admin. But first you need to create
an admin user.

Run bellow command and fill prompted fields to create your first admin user

```shell
docker-compose exec api python manage.py createsuperuser
```

## Importing Dummy Data

Run bellow command to populate database with some dummy data.

```shell
docker-compose exec api python manage.py loaddata dummy.json
```

Note: All the dummy user passwords are `asd12345678`

## API Documentation

To understand api endpoints see `api.yaml` file in root directory.
