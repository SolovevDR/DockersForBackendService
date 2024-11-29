import redis
import json

from session import redis_session


def add_data():
    user_data = {
        "login": "first_user",
        "password": "first_user_password"
    }
    json_data = json.dumps(user_data)
    redis_session.set("user", json_data)
    print("Данные добавлены")


def select_data():
    json_data = redis_session.get("user")
    if json_data:
        user_data = json.loads(json_data)
        print(f"Полученные данные: {user_data}")
    else:
        print("Данные не найдены")


def ping():
    response = redis_session.ping()
    if response:
        print("Подключение успешно!")
    else:
        print("Не удалось подключиться к Redis.")


if __name__ == "__main__":
    try:
        ping()
        add_data()
        select_data()
    except redis.exceptions.RedisError as e:
        print(f"Ошибка: {e}")
