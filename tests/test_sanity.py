import pytest

def test_app_boot(client):
    response = client.get('/')
    assert response.data == b"Hello, World!"

def test_tasks(client):
    response = client.post('/api/process_data')
    task_data = response.get_json()
    print(task_data)
    assert "task_id" in task_data

    response = client.get('/api/tasks/'+ task_data["task_id"])
    print(response.get_json())
