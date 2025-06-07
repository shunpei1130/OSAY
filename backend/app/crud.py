from sqlalchemy.orm import Session
from typing import List, Optional

from . import models, schemas


def get_or_create_student(db: Session, username: str) -> models.Student:
    student = db.query(models.Student).filter(models.Student.username == username).first()
    if not student:
        student = models.Student(username=username)
        db.add(student)
        db.commit()
        db.refresh(student)
    return student


def create_report(db: Session, student: models.Student, text: str, questions: List[str]) -> models.Report:
    db_report = models.Report(text=text, student_id=student.id)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)

    for q in questions:
        db_question = models.Question(text=q, report_id=db_report.id)
        db.add(db_question)
    db.commit()
    db.refresh(db_report)
    return db_report


def store_answers(db: Session, student: models.Student, report_id: int, answers: List[schemas.AnswerCreate]):
    for ans in answers:
        db_ans = models.Answer(question_id=ans.question_id, student_id=student.id, text=ans.text)
        db.add(db_ans)
    db.commit()


def set_report_grade(db: Session, report_id: int, grade: str):
    report = db.query(models.Report).filter(models.Report.id == report_id).first()
    if report:
        report.grade = grade
        db.commit()
        db.refresh(report)
    return report


def list_reports(db: Session):
    return db.query(models.Report).all()


def create_report(db: Session, report: schemas.ReportCreate, questions: List[str]):
    db_report = models.Report(text=report.text)
    db.add(db_report)
    db.commit()
    db.refresh(db_report)

    for q in questions:
        db_question = models.Question(text=q, report_id=db_report.id)
        db.add(db_question)
    db.commit()
    db.refresh(db_report)
    return db_report
