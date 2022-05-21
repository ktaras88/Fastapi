# from fastapi.testclient import TestClient
#
# from .main import app
# from sqlalchemy.orm import Session
#
# client = TestClient(app)
#
#
# def test_read_questions():
#     response = client.get("/questions/")
#     assert response.status_code == 200
#
#
# def test_read_choices():
#     response = client.get('/questions/1')
#     assert response.status_code == 200
#
#
# def test_create_questions():
#     data = {'question_text': 'Question_1?'}
#     response = client.post("/questions/", json=data)
#     assert response.status_code == 200
#     assert response.json()['question_text'] == data['question_text']
#
#
# def test_create_choice():
#     response = client.post('/questions/1/choice/', data={'choice_text': 'choice_1'})
#     response = client.post('/questions/1/choice/', data={'choice_text': 'choice_2'})
#     response = client.post('/questions/1/choice/', data={'choice_text': 'choice_3'})
#
#     count_of_choices = response.json()['choice_text'].count()
#     assert response.status_code == 200
#     assert count_of_choices == 3
