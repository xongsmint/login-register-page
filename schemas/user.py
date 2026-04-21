from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    nickname: str
    email: str
    password: str
