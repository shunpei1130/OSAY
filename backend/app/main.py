from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, Base, get_db
from .openai_client import generate_questions, grade_answers


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/generate", response_model=schemas.Report)
def generate(data: schemas.GenerateRequest, db: Session = Depends(get_db)):
    student = crud.get_or_create_student(db, data.username)
    questions = generate_questions(data.report_text)
    db_report = crud.create_report(db, student, data.report_text, questions)
    return db_report


@app.post("/submit_answers", response_model=schemas.Report)
def submit_answers(payload: schemas.SubmitAnswersRequest, db: Session = Depends(get_db)):
    student = crud.get_or_create_student(db, payload.username)
    crud.store_answers(db, student, payload.report_id, payload.answers)
    report = db.query(models.Report).filter(models.Report.id == payload.report_id).first()
    questions = [q.text for q in report.questions]
    answers = [a.text for a in payload.answers]
    grade = grade_answers(report.text, list(zip(questions, answers)))
    crud.set_report_grade(db, report.id, grade)
    db.refresh(report)
    return report


@app.get("/report/{report_id}", response_model=schemas.Report)
def get_report(report_id: int, db: Session = Depends(get_db)):
    return db.query(models.Report).filter(models.Report.id == report_id).first()


@app.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    reports = crud.list_reports(db)
    return {
        "reports": [
            {
                "id": r.id,
                "student": db.query(models.Student).get(r.student_id).username if r.student_id else None,
                "grade": r.grade,
            }
            for r in reports
        ]
    }

