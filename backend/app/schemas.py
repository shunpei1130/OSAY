from typing import List
from datetime import datetime
from pydantic import BaseModel


class QuestionBase(BaseModel):
    text: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int

    class Config:
        orm_mode = True


class ReportBase(BaseModel):
    text: str


class ReportCreate(ReportBase):
    pass


class Report(ReportBase):
    id: int
    created_at: datetime
    questions: List[Question] = []

    class Config:
        orm_mode = True


class GenerateRequest(BaseModel):
    report_text: str
