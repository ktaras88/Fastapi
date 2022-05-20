from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/questions/", response_model=schemas.Question)
def create_question(question_schema: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db=db, question_schema=question_schema)


@app.get("/questions/", response_model=list[schemas.Question])
def read_questions(limit: int = 5, db: Session = Depends(get_db)):
    return crud.get_questions(db, limit=limit)


@app.post("/questions/{question_id}/choice/", response_model=schemas.Choice)
def create_choice(question_id: int, choice: schemas.ChoiceCreate, db: Session = Depends(get_db)):
    import pdb; pdb.set_trace()
    return crud.create_choice(db=db, choice=choice, question_id=question_id)


@app.get("/questions/{question_id}", response_model=list[schemas.Choice])
def read_choices(question_id: int, db: Session = Depends(get_db)):
    return crud.get_choices(db, question_id=question_id)


@app.get("/questions/{question_id}/votes", response_model=list[schemas.Choice])
def read_voting_results(question_id: int, db: Session = Depends(get_db)):
    return crud.get_voting_results(db, question_id)
