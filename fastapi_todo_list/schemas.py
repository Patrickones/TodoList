from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    batata: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    