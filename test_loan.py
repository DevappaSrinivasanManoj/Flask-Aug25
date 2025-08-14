import pytest
from loan import app

# client -> act as a live server.
@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get('/') # send a get request '/'
    assert resp.status_code == 200
    assert resp.text == "<h1> Loan Approval Application! </h1>"


def test_predict(client):
    test_data= {
                "ApplicantIncome":10,
                "CreditHistory":1.0,
                "Gender":"Male",
                "LoanAmount":111111,
                "Married":"Yes"
                }
    resp = client.post('/predict', json = test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status":'Rejected'}

