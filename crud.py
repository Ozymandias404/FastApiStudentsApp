from sqlalchemy.orm import Session
import models
import schemas


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first() # przenieść do repositories.py


def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email).first() # przenieść do repositories.py


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all() # przenieść do repositories.py


def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(email=student.email, name=student.name, surname=student.surname)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = models.Student(id=student_id, email=student.email, name=student.name, surname=student.surname)
    db.query(models.Student).filter(models.Student.id == student_id).update(student.dict())
    db.commit()
    return db_student


def delete_student(db: Session, student_id: int):
    db.query(models.Student).filter(models.Student.id == student_id).delete()
    db.commit()
    return {"Message": f"Successfully deleted student with id: {student_id}"}


"""
crud.py to serwisy
tutaj dać wyjątki

zrobić katalogi:
db - repositories, models
domain - crud, exceptions
controllers - main, schemas, mappery
"""