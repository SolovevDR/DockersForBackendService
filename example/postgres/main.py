from __future__ import annotations
import asyncio

from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from config import Settings
import crud


async def select_users(async_session: async_sessionmaker):
    async with async_session() as session:
        result = await crud.select_users(session=session)
        print("Список пользователей:")
        for user in result:
            print(user)


async def select_roles(async_session: async_sessionmaker):
    async with async_session() as session:
        result = await crud.select_roles(session=session)
        print("Список ролей:")
        for role in result:
            print(role)


async def add_user(async_session: async_sessionmaker):
    async with async_session() as session:
        await crud.add_user(
            session=session,
            login="user_3",
            password="password_3",
            role=2,
            comment="user №3"
        )
        print("Пользователь добавлен")


async def add_role(async_session: async_sessionmaker):
    async with async_session() as session:
        await crud.add_role(session=session, role_name="test")
        print("Роль добавлена")


async def update_user(async_session: async_sessionmaker):
    async with async_session() as session:
        await crud.update_user(
            session=session,
            user_id=3,
            login="test user",
            password="password 3 password"
        )
        print("Пользователь обновлен")


async def update_role(async_session: async_sessionmaker):
    async with async_session() as session:
        await crud.update_role(session=session, role_id=3, role_name="TEST")
        print("Список ролей:")


async def async_main() -> None:
    engine = create_async_engine(
        (
            f"postgresql+asyncpg://{Settings.db_user}:{Settings.db_pass}@"
            f"{Settings.db_host}:{Settings.db_port}/{Settings.db_name}"
        ),
        echo=True,
    )
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    await add_user(async_session=async_session)
    await add_role(async_session=async_session)
    await update_user(async_session=async_session)
    await update_role(async_session=async_session)
    await select_users(async_session=async_session)
    await select_roles(async_session=async_session)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
