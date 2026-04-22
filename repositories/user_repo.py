from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from pydantic import EmailStr
from schemas.user import UserSchema
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserSchema
import logging

logger = logging.getLogger(__name__)

class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserRepo:
    def __init__(self, session: Session):
        self.session = session
    
    def _get_user_by(self, **kwargs) -> User | None:
        return self.session.execute(
            select(User).filter_by(**kwargs)
        ).scalar_one_or_none()

    def get_by_id(self, user_id: int) -> User:
        user = self._get_user_by(id=user_id)
        if not user:
            raise UserNotFoundError(f"User with id '{user_id}' not found.")
        return user

    def get_by_email(self, email: EmailStr) -> User:
        user = self._get_user_by(email=email)
        if not user:
            raise UserNotFoundError(f"User with email '{email}' not found.")
        return user
    
    def register_user(self, email: EmailStr, password: str, nickname: str) -> User:
        """Returns user.serialize() or raise error"""

        if self._get_user_by(email=email):
            raise UserAlreadyExistsError(f"User with email '{email}' already exists.")

        user = User(email=email, nickname=nickname)
        user.password = password

        try:
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except Exception as e:
            self.session.rollback()
            logger.error(f"Failed to register user: {e}")
            raise

    def login(self, email: EmailStr, password: str) -> bool:
        try:
            user = self.get_by_email(email=email)
            return user.check_password(plain=password)
        except UserNotFoundError:
            raise
