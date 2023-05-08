from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from controllers import schemas
from domain import crud
from db import models
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_students(db=db, skip=skip, limit=limit)


@app.post("/students/", response_model=schemas.Student, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)


@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db=db, student_id=student_id)


@app.put("/students/{student_id}", response_model=schemas.Student, status_code=status.HTTP_200_OK)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.update_student(db=db, student_id=student_id, student=student)


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db=db, student_id=student_id)
