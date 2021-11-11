from app import *
import requests

def test_index():
    
    # more intreesting way to test the the page works
	client = app.test_client()
	response = client.get("/")
	assert response.status_code == 200  # success
