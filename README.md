# 概要

練習用

## 使用技術

- FastAPI
- GraphQL
- Docker

## セットアップ

```shell
pipenv --python 3.9
```

```shell
pipenv install fastapi uvicorn SQLAlchemy graphene graphene-sqlalchemy
```

```shell
pipenv install yapf flake8 --dev
```

```shell
pipenv shell
```

```shell
docker-compose up
```

```shell
docker-compose exec app bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
