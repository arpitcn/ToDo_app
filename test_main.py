from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


data_create = {
    'title': "test title",
    'description': 'testing description'
}
ID = None

def test_create_task_view():
    response = client.post("/", json=data_create)
    assert response.status_code == 200
    global ID
    ID = response.json()['id']
    assert response.json() == {
        'id':ID,
        'title': "test title",
        'description': 'testing description'
    }


def test_todo_list():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()[-1] == {
        'id': ID,
        'title': "test title",
        'description': 'testing description'
    }


def test_get_task_view():
    response = client.get("/task/"+str(ID))
    assert response.status_code == 200
    assert response.json() == {
        'id': ID,
        'title': "test title",
        'description': 'testing description'
    }


def test_update_task_view():
    data_update = {'id': ID, 'title': 'updated task', 'description': 'updated description'}
    response = client.put("/task/", json=data_update)
    assert response.status_code == 200
    assert response.json() == {
        'id': ID,
        'title': "updated task",
        'description': 'updated description'
    }



def test_delete_task_view():
    response = client.delete("/task/"+str(ID))
    assert response.status_code == 200
    assert response.json() == {"message": "Task successfully deleted"}

