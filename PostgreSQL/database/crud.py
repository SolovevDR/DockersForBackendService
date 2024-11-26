from sqlalchemy.ext.asyncio import AsyncSession

from models import User


async def add_user(session: AsyncSession, user_data: dict) -> None:
    user = User(**user_data)
    session.add(user)

    try:
        await session.commit()
    except Exception as e:
        await session.rollback()
        print(f"Ошибка при добавлении данных: {e}")
    finally:
        await session.close()
