from sqlalchemy.orm import Session

from . import models, schemas


def get_questions(db: Session, limit: int = 5):
    # return db.query(models.Question).limit(limit).all()
    return db.query(models.Question).all()


def get_choices(db: Session, question_id: int):
    return db.query(models.Choice).filter(models.Choice.question_id == question_id).all()


def make_vote(db: Session, question_id: int, vote: schemas.Vote):
    selected_choice = db.query(models.Choice).filter(models.Choice.question_id == question_id).get(models.Choice.id == vote.choice)

    selected_choice.votes += 1
    db.add(selected_choice)
    db.commit()
    return selected_choice


def get_voting_results(db: Session, question_id: int):
    return db.query(models.Choice).filter(models.Choice.question_id == question_id).all()


def create_question(db: Session, question_schema: schemas.QuestionCreate):
    db_question = models.Question(question_text=question_schema.question_text, pub_date=question_schema.pub_date)
    db.add(db_question)
    db.commit()
    return db_question


def create_choice(db: Session, choice: schemas.ChoiceCreate, question_id: int):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if question.answer_count < 3:
        question.answer_count += 1
        db_choice = models.Choice(**choice.dict(), question_id=question_id)
        db.add(db_choice)
        db.add(question)
        db.commit()
        db.refresh(question)
        return db_choice
