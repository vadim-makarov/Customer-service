"""Contains unit tests"""
import allure
import pytest

from app.models import User, Service, Review
from app.sms import send_sms


@pytest.mark.unit
class TestUnit:
    """Contains a common logic unit tests"""

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("User creates in DB")
    def test_user_exist_in_db(self, user_in_db: User):
        """Checks if DB creates and user can appear in it"""
        check_user = User.query.filter_by(username=user_in_db.username).first()
        assert check_user.username, 'Username is empty'
        assert check_user.phone_number, 'Phone number is empty'

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Password hashes correctly")
    def test_password_hashing(self, user_in_db: User):
        """Checks a password hashing method"""
        user_in_db.set_password('password')
        assert user_in_db.check_password('password'), 'Right password was not accepted'
        assert not user_in_db.check_password('hassword'), 'Wrong password was accepted'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("SMS generates correctly")
    def test_send_sms(self):
        """Checks a send sms method """
        code = send_sms('+555555')
        nums = [i.isnumeric() for i in code]
        assert len(code) == 4, 'sms code longer or shorter than 4'
        assert all(nums), 'one of sms code symbols is not numeric'

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Service creates in DB")
    def test_user_has_service(self, user_in_db: User, service_in_db: Service):
        """Checks that service creates in DB"""
        first_service = Service.query.filter_by(user_id=user_in_db.id).first()
        assert first_service.user_id == user_in_db.id, f'{user_in_db.username} has no any service'

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Review creates in DB")
    def test_user_has_review(self, review_in_db):
        """Checks that review creates in DB"""
        reviews = Review.query.order_by(Review.review_date.desc()).all()
        assert len(reviews) > 0, 'There is no any reviews'
