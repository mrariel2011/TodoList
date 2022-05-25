# Create your tests here.
def test_something(client, db):
    # response = client.get('/some_url_defined_in_test_urls/').content
    response = client.get("/tasks/")

    assert response.status_code == 302

