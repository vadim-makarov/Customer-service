from app.models import User
from app.sms import send_sms


class TestUser:
    def test_user_exist_in_db(self, create_db):
        user = User(username='Vinnie', phone_number='The Pooh')
        create_db.create_all()
        create_db.session.add(user)
        create_db.session.commit()
        check_user = User.query.filter_by(username='Vinnie').first()
        assert check_user.username == 'Vinnie', 'Username is unexpected'
        assert check_user.phone_number == 'The Pooh', 'Phone number is incorrect'

    def test_password_hashing(self):
        user = User(username='John Snow')
        user.set_password('password')
        assert user.check_password('password'), 'Right password was not accepted'
        assert not user.check_password('hassword'), 'Wrong password was accepted'

    def test_send_sms(self):
        code = send_sms('+555555')
        nums = [i.isnumeric() for i in code]
        assert len(code) == 4, 'sms code longer or shorter than 4'
        assert all(nums), 'one of sms code symbols is not numeric'
