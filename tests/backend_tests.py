from app import db
from app.models import User
from app.sms import send_sms


class TestUser:
    def test_user_exist_in_db(self, user):
        db.create_all()
        db.session.add(user)
        db.session.commit()
        check_user = User.query.filter_by(username=user.username).first()
        assert check_user.username, 'Username is empty'
        assert check_user.phone_number, 'Phone number is empty'

    def test_password_hashing(self, user):
        user.set_password('password')
        assert user.check_password('password'), 'Right password was not accepted'
        assert not user.check_password('hassword'), 'Wrong password was accepted'

    def test_send_sms(self):
        code = send_sms('+555555')
        nums = [i.isnumeric() for i in code]
        assert len(code) == 4, 'sms code longer or shorter than 4'
        assert all(nums), 'one of sms code symbols is not numeric'
    #
    # def test_user_has_service(self, user, service):
    #     service = Service.query.filter_by(user_id=user.id).first()
    #     assert service.user_id == user.id, 'Vinnie the user has no any service'
    #
    # def test_user_has_review(self, user, review):
    #     reviews = Review.query.order_by(Review.review_date.desc()).all()
    #     assert len(reviews) > 0, 'There is no any reviews'
