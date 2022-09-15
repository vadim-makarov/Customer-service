from app import db
from app.models import User, Service, Review
from app.sms import send_sms


class TestUser:
    def test_user_exist_in_db(self, user: User):
        db.session.add(user)
        db.session.commit()
        check_user = User.query.filter_by(username=user.username).first()
        assert check_user.username, 'Username is empty'
        assert check_user.phone_number, 'Phone number is empty'

    def test_password_hashing(self, user: User):
        user.set_password('password')
        assert user.check_password('password'), 'Right password was not accepted'
        assert not user.check_password('hassword'), 'Wrong password was accepted'

    def test_send_sms(self):
        code = send_sms('+555555')
        nums = [i.isnumeric() for i in code]
        assert len(code) == 4, 'sms code longer or shorter than 4'
        assert all(nums), 'one of sms code symbols is not numeric'

    def test_user_has_service(self, user: User, service: Service):
        service = Service.query.filter_by(user_id=user.id).first()
        assert service.user_id == user.id, f'{user.username} has no any service'

    def test_user_has_review(self, user: User, review: Review):
        reviews = Review.query.order_by(Review.review_date.desc()).all()
        assert len(reviews) > 0, 'There is no any reviews'

# def test_request_with_logged_in_user(app, user):
#     user = User.query.get(1)
#     with app.test_client(user=user) as client:
#         # This request has user 1 already logged in!
#         client.get("/main/index")

