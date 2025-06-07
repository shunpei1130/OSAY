from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, Base, get_db
from .openai_client import generate_questions

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/generate", response_model=schemas.Report)
def generate(report: schemas.GenerateRequest, db: Session = Depends(get_db)):
    questions = generate_questions(report.report_text)
    db_report = crud.create_report(db, schemas.ReportCreate(text=report.report_text), questions)
    return db_report
