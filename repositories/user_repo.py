from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User

class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_email(self, email: str) -> User | None:
        return self.session.scalar(
            select(User).where(User.email == email)
        )

    def create(self, nickname: str, email: str, password: str) -> User:
        new_user = User(nickname=nickname, email=email)
        new_user.password = password

        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)

        return new_user

    def email_exists(self, email: str) -> bool:
        return self.get_by_email(email) is not None
