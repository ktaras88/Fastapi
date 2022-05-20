from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)
    pub_date = Column(DateTime, default=datetime.now())
    answer_count = Column(Integer, default=0)

    choices = relationship("Choice", back_populates="question")

    def __str__(self):
        return self.question_text


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String)
    votes = Column(Integer, default=0)
    question_id = Column(Integer, ForeignKey("questions.id"))

    question = relationship("Question", back_populates="choices")

    def __str__(self):
        return self.choice_text
