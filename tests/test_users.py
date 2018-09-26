import unittest

from src.users import validate_password, validate_user_name, validate_email,\
    validate_name, check_age, check_sex, create_user, login


class TestUser(unittest.TestCase):

    #Tests for checking password
    def test_validate_password(self):
        valid = validate_password('Aq4@')
        self.assertEqual(valid, 'Aq4@')

    def test_validate_pass_wrong_format(self):
        valid = validate_password('Ae3')
        self.assertEqual(400, valid)

    def test_validate_pass_empty_field(self):
        valid = validate_password('')
        self.assertEqual(401, valid)

    #Tests for checking username
    def test_validate_username(self):
        valid = validate_user_name('fahad2#')
        self.assertEqual(valid, 'fahad2#')

    def test_validate_username_wrong_format(self):
        valid = validate_user_name('fah')
        self.assertEqual(400, valid)

    def test_validate_username_empty_field(self):
        valid = validate_user_name('')
        self.assertEqual(401, valid)

    # Tests for checking email
    def test_validate_email(self):
        valid = validate_email('johndoe@mail.com')
        self.assertEqual(valid, 'johndoe@mail.com')

    def test_validate_email_empty_field(self):
        valid = validate_email('')
        self.assertEqual(401, valid)

    def test_validate_email_wrong_format(self):
        valid = validate_email('2johndoe2@mail.co.mhkj')
        self.assertEqual(400, valid)

    # Tests for checking name
    def test_validate_name(self):
        valid = validate_name('Denis Mab')
        self.assertEqual(valid, 'Denis Mab')

    def test_validate_name_empty_field(self):
        valid = validate_name('')
        self.assertEqual(401, valid)

    def test_validate_name_wrong_format(self):
        valid = validate_name('mail5co')
        self.assertEqual(400, valid)

    # Tests for checking age
    def test_check_age(self):
        valid = check_age(8)
        self.assertEqual(valid, 8)

    def test_check_age_empty_field(self):
        valid = check_age('')
        self.assertEqual(401, valid)

    def test_check_age_wrong_format(self):
        valid = check_age('mail5co')
        self.assertEqual(400, valid)

    def test_check_age_below_zero(self):
        valid = check_age(-12)
        self.assertEqual(400, valid)

    # Tests for checking sex
    def test_check_sex(self):
        valid = check_sex('male')
        self.assertEqual(valid, 'male')

    def test_check_sex_empty_field(self):
        valid = check_sex('')
        self.assertEqual(401, valid)

    def test_check_sex_wrong_format(self):
        valid = check_sex('mail5co')
        self.assertEqual(400, valid)

    # Tests for creating user
    def test_create_user(self):
        valid = create_user('fahad', 'fahads', 6, 'johndoe@mail.com', 'Aq4@', 'male')
        self.assertEqual('fahad user has been created', valid)

    def test_create_user_user_exists(self):
        valid = create_user('fahad', 'fahad', 6, 'johndoe@mail.com', 'Aq4@', 'male')
        self.assertEqual('username should not be the  same as the name', valid)

    def test_create_user_empty_field(self):
        valid = create_user('', 'sskjhskh', 45, 'johndoe@mail.com', 'Aq4@', 'male')
        self.assertEqual('Please fill in the missing fields', valid)

    def test_create_user_wrong_format(self):
        valid = create_user('Denis Mab', 'shgjshs', 12, 'johndoe@mail.com', 'sjhshs', 'uyu')
        self.assertEqual('Please fill in the correct information', valid)

    # Tests for log in user
    def test_login_user(self):
        valid1 = create_user('Denis Mab', 'shgjshsd', 12, 'johndoe@mail.com', 'Ar4@', 'male')
        valid2 = login('shgjshs', 'Aq4@')
        self.assertEqual('User Name and Password do not match', valid2)

    def test_login_user_empty_field(self):
        valid = login('fahad', '')
        self.assertEqual('Please fill in the missing fields', valid)

    def test_login_user_wrong_format(self):
        valid = login('fahad', 67665)
        self.assertEqual('Please fill in the correct information', valid)
    #
