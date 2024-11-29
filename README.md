# DockersForBackendService

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

## About
This is a repository with containers for backend components. 
It is intended for testing and development, not for use on the prod.

P.S. in project you can see `.env` file in directory. Don't do this in real project. 
This is done for a better understanding of the project.

### The repository contains the following components:
* **[About](#About)**
* **[PostgresSQL](#PostgresSQL)**
    * [PostgresSQL-Start](#PostgresSQL-Start)
    * [Create-alembic-migration](#Create-alembic-migration)
    * [PostgresSQL-Down](#PostgresSQL-Down)
* **[Redis](#Redis)**
    * [Redis-Start](#Redis-Start)
    * [Redis-Down](#Redis-Down)
* **[Example](#Example)**
    * [PostgresSQL example](#PostgresSQL example)
    * [Redis example](#Redis example)


## PostgresSQL

---

### PostgresSQL Start

1. edit the `/PostgresSQL/.db.env` file. 
Replace the following variables in it if you need to create a user with parameters.
```.dotenv
POSTGRES_USER=test_user
POSTGRES_PASSWORD=pg_pass
POSTGRES_DB=pg_db

DB_HOST=localhost
DB_NAME=pg_db
DB_USER=test_user
DB_PASS=pg_pass
```

If you want to create tables immediately after 
starting the container, you need to edit the 
`IS_INIT_DATA_ALEMBIC=True` variable.

You can also fill the table using a Python script, 
edit the `IS_INIT_DATA_PYTHON=True` variable for this one.

2. Go to the directory `PostgresSQL`
```shell
cd PostgresSQL
```
3. Then run the command.
```shell
docker-compose up -d --build
```
---

### Create alembic migration

1. Edit the `IS_INIT_DATA_ALEMBIC=False` and `IS_INIT_DATA_PYTHON=False` variables in 
file `/PostrgresSQL/.db.env`.
2. Go to the directory `PostgresSQL`
```shell
cd PostgresSQL
```
3. Run the command.
```shell
docker-compose up -d --build
```
4. Describe it in the `Postgres/database/models.py` file your tables like this

```python
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    login = Column(String)
    password = Column(String)
    comment = Column(String, nullable=True)
    role = Column(Integer, ForeignKey("role.id"))

    role_id = relationship("Role", back_populates="owner")


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)

    owner = relationship("User", back_populates="role_id")
```
5. Run the command.
```shell
alembic revision --autogenerate -m "<migration name>"
```
6. Turn off the docker container
```shell
docker-compose down -v
```
7. Edit the `IS_INIT_DATA_ALEMBIC=True` variable in file `/PostrgresSQL/.db.env`.
8. Run the command.
```shell
docker-compose up -d --build
```
---

### PostgresSQL Down
1. Go to the directory `PostgresSQL`
```shell
cd PostgresSQL
```
2. Run the command.
```shell
docker-compose down -v
```


## Redis
---
---

### Redis Start

1. edit the `/Redis/.redis.env` file. 
Replace the following variables in it if you need to create a user with parameters.
```.dotenv
REDIS_PASSWORD=my_redis_password
REDIS_USER=my_user
REDIS_USER_PASSWORD=my_user_password
```

2. Go to the directory `Redis`
```shell
cd PostgresSQL
```
3. Then run the command.
```shell
docker-compose up -d --build
```

---
### Redis Down

1. Go to the directory `Redis`
```shell
cd Redis
```
2. Run the command.
```shell
docker-compose down
```
---

## Example

The simple example of use containers using python script. 

### PostgresSQL example
Contains examples of the following scripts:
* add_user
* select_users
* update_user
* add_role
* select_roles
* update_role

### Redis example
Contains examples of the following scripts:
* ping redis
* add_data
* select_data
