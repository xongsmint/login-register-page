from sqlalchemy.orm import Session
from repositories.user_repo import UserRepository
from models.user import User

class AuthService:
    def __init__(self, session: Session) -> None:
        self.repo = UserRepository(session)

    def register(self, nickname: str, email: str, password: str) -> User:
        if self.repo.email_exists(email):
            raise ValueError(f"O email '{email}' já está em uso.")
        return self.repo.create(nickname, email, password)
    
    def login(self, email: str, password: str) -> User:
        user = self.repo.get_by_email(email)
        if not user or not user.verify_password(password):
            raise ValueError("Email ou senha inválidos.")
        return user
