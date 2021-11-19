# Yemeksepeti API

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
```
docker-compose up -d

# Optionally you can check if container running by following command
docker ps |grep yemeksepeti-api
```

Run below command to apply migrations
```
docker-compose exec api python manage.py migrate
```
