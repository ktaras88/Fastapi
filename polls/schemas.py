from pydantic import BaseModel
from datetime import datetime


class ChoiceBase(BaseModel):
    choice_text: str
    votes: int = 0


class ChoiceCreate(ChoiceBase):
    pass


class Choice(ChoiceBase):
    id: int
    question_id: int

    class Config:
        orm_mode = True


class QuestionBase(BaseModel):
    question_text: str
    pub_date: datetime = datetime.now()


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    # choices: list[Choice] = []

    class Config:
        orm_mode = True
