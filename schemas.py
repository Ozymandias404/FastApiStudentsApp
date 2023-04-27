from pydantic import BaseModel


class StudentBase(BaseModel):
    email: str
    name: str
    surname: str


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

