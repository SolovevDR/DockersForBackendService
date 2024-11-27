#!/bin/bash

# Проверка переменных окружения
if [[ -z "$REDIS_PASSWORD" || -z "$REDIS_USER" || -z "$REDIS_USER_PASSWORD" ]]; then
  echo "Error: REDIS_PASSWORD, REDIS_USER, and REDIS_USER_PASSWORD environment variables must be set."
  exit 1
fi

# Создание директории, если она не существует
mkdir -p /usr/local/etc/redis

# Создание и запись в redis.conf
cat > /usr/local/etc/redis/redis.conf << EOF
bind 0.0.0.0
requirepass "$REDIS_PASSWORD"
appendonly yes
appendfsync everysec

EOF

# Создание и запись в users.acl  - ИЗМЕНЕНО!
cat > /usr/local/etc/redis/users.acl << EOF
user default on nopass ~* +@all
user ${REDIS_USER} on >${REDIS_USER_PASSWORD} ~* +@all

EOF

# Запуск redis-server.  Обработка ошибок.  Выводит больше информации об ошибках.
redis-server /usr/local/etc/redis/redis.conf --aclfile /usr/local/etc/redis/users.acl
