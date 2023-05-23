import time

from db import models
from controllers import schemas
from sqlalchemy.orm import Session
from db.database import engine, db_meta


def get_first_student_with_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_first_student_with_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first()


def get_all_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def create_student_with_data(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(email=student.email, name=student.name, surname=student.surname)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student_with_id(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = models.Student(id=student_id, email=student.email, name=student.name, surname=student.surname)
    db.query(models.Student).filter(models.Student.id == student_id).update(student.dict())
    db.commit()
    return db_student


def delete_student_with_id(db: Session, student_id: int):
    db.query(models.Student).filter(models.Student.id == student_id).delete()
    db.commit()
    return {"Message": f"Successfully deleted student with id: {student_id}"}


def clear_data(db: Session):
    db.query(models.Student).delete()
    db.commit()
