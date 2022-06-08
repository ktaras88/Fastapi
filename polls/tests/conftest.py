import pytest
from fastapi.testclient import TestClient

from .database_test import TestingSessionLocal
from .. import models
from ..main import app


client = TestClient(app)


@pytest.fixture
def question_id():
    data = {'question_text': 'Test_Question?'}
    response = client.post("/questions/", json=data)
    return response.json()['id']


@pytest.fixture
def database_cleanup():
    db = TestingSessionLocal()
    db.query(models.Question).delete()
    db.query(models.Choice).delete()
    db.commit()
