from fastapi.testclient import TestClient
from main import app
import httpx

client = TestClient(app)



def test_get_all_posts():
    response = client.get('/blog/all')
    assert response.status_code == 200

def test_auth_error():
    response = client.post('/token',data=
    {
        'username':'',
        'password':''
    }
    )
    access_token = response.json().get('access_token')
    assert access_token == None
    assert response.json().get('detail')[0].get('msg') == 'Field required'