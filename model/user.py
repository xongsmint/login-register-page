from pydantic import EmailStr
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from database.database import Base
import bcrypt

class User(Base):
    __tablename__ = "users"

    id:            Mapped[int]      = mapped_column(primary_key=True)
    email:         Mapped[EmailStr] = mapped_column(unique=True, nullable=False)
    nickname:      Mapped[str]      = mapped_column(nullable=False)
    password_hash: Mapped[str]      = mapped_column(nullable=False)

    @hybrid_property
    def password(self) -> None:
        raise AttributeError("Password is write-only.")

    @password.setter
    def password(self, plain: str) -> None:
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(
            plain.encode("utf-8"),
            salt
        ).decode("utf-8")
    
    def check_password(self, plain: str) -> bool:
        return bcrypt.checkpw(plain.encode("utf-8"), self.password_hash.encode("utf-8"))
