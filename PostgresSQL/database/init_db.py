from __future__ import annotations

import asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from config import Settings
from crud import add_user


async def add_users(async_session):
    async with async_session() as session:
        user_data = {
                "login": Settings.second_user_login,
                "password": Settings.second_user_password,
                "role": Settings.second_user_role
            }
        await add_user(session=session, user_data=user_data)


async def async_main() -> None:
    engine = create_async_engine(
        (
            f"postgresql+asyncpg://{Settings.db_user}:{Settings.db_pass}@"
            f"{Settings.db_host}:{Settings.db_port_local}/{Settings.db_name}"
        ),
        echo=True,
    )
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    await add_users(async_session=async_session)


loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
