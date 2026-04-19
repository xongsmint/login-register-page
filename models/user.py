from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
import bcrypt

class User(Base):
    __tablename__ = "users"

    id:            Mapped[int] = mapped_column(primary_key=True)
    nickname:      Mapped[str] = mapped_column(nullable=False)
    email:         Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is write-only.")
    
    @password.setter
    def password(self, plain_password: str) -> None:
        self.password_hash = bcrypt.hashpw(
            plain_password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            self.password_hash.encode("utf-8")
        )
