# Yemeksepeti


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
