from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Role
from scheme import OneRole, ListrRoles, OneUser, ListUsers


async def select_users(session: AsyncSession) -> ListUsers:
    query = (
        select(
            User.id,
            User.login,
            User.password,
            User.comment,
            Role.name.label("role_name")
        )
        .join(User.role_id)
    )
    result = await session.execute(query)
    result = result.all()
    result = [OneUser.from_orm(_) for _ in result]
    return result


async def select_roles(session: AsyncSession) -> ListrRoles:
    query = select(Role)
    result = await session.scalars(query)
    result = result.all()
    result = ListrRoles(roles=result)
    return result


async def add_user(
    session: AsyncSession, login: str, password: str, role: int, comment: str = None
) -> None:
    user = User(
        id=3,
        login=login,
        password=password,
        comment=comment,
        role=role
    )
    session.add(user)
    await session.commit()


async def add_role(session: AsyncSession, role_name: str) -> None:
    role = Role(name=role_name, id=3)
    session.add(role)
    await session.commit()


async def update_user(
    session: AsyncSession,
    user_id: int,
    login: str = None,
    password: str = None,
    comment: str = None,
    role: int = None
) -> None:
    update_data = {}
    if login:
        update_data["login"] = login
    if password:
        update_data["password"] = password
    if comment:
        update_data["comment"] = comment
    if role:
        update_data["role"] = role
    query = update(User).values(update_data).filter(User.id == user_id)
    await session.execute(query)
    await session.commit()


async def update_role(session: AsyncSession, role_id: int, role_name: str) -> None:
    query = update(Role).values({"name": role_name}).filter(Role.id == role_id)
    await session.execute(query)
    await session.commit()

