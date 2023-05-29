from sqlalchemy.orm import Session
from db import models
from controllers import schemas
from controllers import repositories
from fastapi import Depends, FastAPI, HTTPException, status


def get_student(db: Session, student_id: int):
    db_student = repositories.get_first_student_with_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return repositories.get_all_students(db, skip, limit)


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = repositories.get_first_student_with_email(db, email=student.email)
    if db_student:
        raise HTTPException(status_code=400, detail="Email already registered")
    return repositories.create_student_with_data(db=db, student=student)


def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = repositories.get_first_student_with_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return repositories.update_student_with_id(db, student_id=student_id, student=student)


def delete_student(db: Session, student_id: int):
    db_student = repositories.get_first_student_with_id(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return repositories.delete_student_with_id(db, student_id=student_id)
