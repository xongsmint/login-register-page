from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    nickname: str
    email: EmailStr
    password: str
