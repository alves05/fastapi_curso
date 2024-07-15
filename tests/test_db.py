from sqlalchemy import select

from fastapi_curso.models import User


def test_create_user(session):
    user = User(
        username='usertest',
        email='usertest@email.com',
        password='passwordtest',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'usertest@email.com')
    )

    assert result.username == 'usertest'
