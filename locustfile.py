w3from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)  # Time between requests
    host = "http://localhost:5000/"  # Specify the base host URL

    @task
    def index(self):
        self.client.get("/")  # Make a GET request to the homepage
