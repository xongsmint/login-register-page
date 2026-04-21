from pydantic import EmailStr
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from database.database import Base
import bcrypt
from datetime import datetime

class User(Base):
    __tablename__ = "users"


    id:            Mapped[int]      = mapped_column(primary_key=True)
    email:         Mapped[str]      = mapped_column(unique=True, nullable=False)
    nickname:      Mapped[str]      = mapped_column(nullable=False)
    password_hash: Mapped[str]      = mapped_column(nullable=False)
    created_at:    Mapped[datetime] = mapped_column(default=lambda: datetime.now(), nullable=False)
    is_active:     Mapped[bool]     = mapped_column(default=True, nullable=False)

    @hybrid_property
    def password(self) -> None:
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, plain: str):
        salt = bcrypt.gensalt(rounds=12)
        self.password_hash = bcrypt.hashpw(
            plain.encode("utf-8"),
            salt
        ).decode("utf-8")
    
    def check_password(self, plain: str) -> bool:
        return bcrypt.checkpw(plain.encode("utf-8"), self.password_hash.encode("utf-8"))

    def serialize(self) -> dict:
        return {
            "id":         self.id,
            "email":      self.email,
            "nickname":   self.nickname,
            "is_active":  self.is_active,
            "created_at": self.created_at.isoformat(),
        }
    
    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email!r}>"
