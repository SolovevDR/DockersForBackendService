import redis

from config import Settings

redis_session = redis.Redis(
    host=Settings.host,
    port=Settings.port,
    db=0,
    username=Settings.redis_user,
    password=Settings.redis_user_password
)
