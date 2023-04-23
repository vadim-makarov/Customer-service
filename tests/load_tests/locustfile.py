"""Contains a load scenario class"""

from locust import HttpUser, task, between


class Pages(HttpUser):
    """Contains a user activity scenarios"""
    wait_time = between(2, 3)

    @task(2)
    def main_page(self):
        """Opens a main page"""
        self.client.get("/main/index")

    @task
    def review_page(self):
        """Opens a review page"""
        self.client.get("/main/reviews")

    @task
    def prices(self):
        """Opens a prices page"""
        self.client.get('/main/pricing')
