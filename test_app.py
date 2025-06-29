import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_create_event(client):
    response = client.post('/events', json={
        'title': 'Meeting',
        'description': 'Team sync-up',
        'start_time': '2025-06-29T15:00:00',
        'end_time': '2025-06-29T16:00:00'
    })
    assert response.status_code == 201
