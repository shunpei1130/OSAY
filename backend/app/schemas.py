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


class Student(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class Report(ReportBase):
    id: int
    created_at: datetime
    questions: List[Question] = []
    grade: str | None = None

    class Config:
        orm_mode = True


class GenerateRequest(BaseModel):
    username: str
    report_text: str


class AnswerCreate(BaseModel):
    question_id: int
    text: str


class SubmitAnswersRequest(BaseModel):
    username: str
    report_id: int
    answers: List[AnswerCreate]
