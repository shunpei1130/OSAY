from sqlalchemy.orm import Session
from typing import List

from . import models, schemas


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
