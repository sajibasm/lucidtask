from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class PostBase(BaseModel):
    text: constr(max_length=1048576)  # Limit validation to 1 MB in size

    class Config:
        from_attributes = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
