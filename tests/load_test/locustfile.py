from locust import HttpUser, task, between


class Pages(HttpUser):
    wait_time = between(2, 3)

    # @staticmethod
    # def user():
    #     username = ''.join(random.sample(string.ascii_lowercase, 8))
    #     phone_number = '+' + ''.join(random.sample(string.digits * 3, 11))
    #     user = User(username=username, phone_number=phone_number)
    #     return user
    #
    # def on_start(self):
    #     db.session.add(self.user())
    #     db.session.commit()
    #
    # @task
    # def user_page(self):
    #     self.client.get(f'/user/{self.user()}')

    @task(2)
    def main_page(self):
        self.client.get("/main/index")

    @task
    def review_page(self):
        self.client.get("/main/reviews")

    @task
    def prices(self):
        self.client.get('/main/pricing')
