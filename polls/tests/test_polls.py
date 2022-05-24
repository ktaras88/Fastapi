from fastapi.testclient import TestClient

from .database_test import TestingSessionLocal, engine
from .. import models
from ..database import Base
from ..main import app, get_db

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
db = TestingSessionLocal()
client = TestClient(app)


def test_read_questions(database_cleanup):
    response = client.get("/questions/")
    assert response.status_code == 200
    assert response.context['questions'] == []


def test_read_choices():
    response = client.get('/questions/1')
    question_id = 1
    assert response.status_code == 200
    assert response.context['question_id'] == question_id


def test_create_questions():
    data = {'question_text': 'Question_1?'}
    response = client.post("/questions/", json=data)
    assert response.status_code == 200
    assert response.json()['question_text'] == data['question_text']


def test_create_choice(question_id):
    response = None
    for num in range(3):
        choice = f'test_choice_{num}'
        response = client.post(f'/questions/{question_id}/choice/', json={'choice_text': choice})
    count_of_choices = db.query(models.Choice).filter(models.Choice.question_id == question_id).count()
    assert response.status_code == 200
    assert count_of_choices == 3
