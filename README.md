# Delivery Application

Example food order application

## Pre Requirements

You need to have [docker](https://www.docker.com) and [docker-compose](https://docs.docker.com/compose/install/) 
installed in your system to deploy this project.

## Folder Structure

```
├── README.md                             # you are reading this :)
├── .env                                  # environment variables used by docker-compse.yml
├── api.yml                               # API endpoint documentation
├── docker-compose.yml                    # docker service definitions
└── api                                   # application folder
    ├── Dockerfile
    ├── requirements.txt                  # python package requirements
    ├── configuration                     # includes django settings and url definitions
    ├── dummy.json                        # dummy data for populating database 
    ├── order                             # includes order related views and models
    │   ├── consumers.py                  # includes order consumers
    │   ├── management
    │   │   └── commands
    │   │       └── startconsumers.py     # this command starts consumers for listening pub-sub events
    ├── restaurant                        # includes restaurnat related views and models
    └── utils
        └── redis.py                      # includes client for pub-sub operations
```

## Environment Variables

For development you dont need to change environment variables.

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
| REDIS_HOST    | redis     | X        | Redis host for pub sub actions                                                                  |
| REDIS_PORT    | 6379      | X        | Redis port for pub sub actions                                                                  |

## Installation

This command download and install necessary image and packages.

```
docker-compose build
```

## Starting Application

Start containers with `docker-compose up -d`

This will start 4 containers `redis` for pub-sub operations, `postgresql` as database, a django application which 
acts as rest api (see **API** section) and another django process which act as consumer to process orders.

## Database Migration

After application started in background with `docker-compose up -d`
Note: You can check if container running by `docker ps |grep delivery-api`

Run below command to apply migrations

```shell
docker-compose exec api python manage.py migrate
```

## Creating Admin User

Django comes with admin interface, to access it you can go to http://localhost:8080/admin

Run bellow command and fill prompted fields to create your first admin user

```shell
docker-compose exec api python manage.py createsuperuser
```

## Importing Dummy Data

Run bellow command to populate database with some dummy data.

```shell
docker-compose exec api python manage.py loaddata dummy.json
```

After this import you can access admin interface with user `admin@admin.com` and password `12345678`

## API Documentation

To understand api endpoints see `api.yaml` file in root directory.

## Running Linter

```shell
docker-compose exec api flake8 .
```
