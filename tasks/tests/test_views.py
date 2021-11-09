
# Create your tests here.
def test_something(client):
    #response = client.get('/some_url_defined_in_test_urls/').content
    response = client.get('/tasks/')

    assert response.status_code == 200
    assert 'tasks list' in response.content.decode("utf-8") 

