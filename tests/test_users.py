import unittest

from src.users import validate_password, validate_user_name, validate_email, validate_name, check_age, check_sex


class TestUser(unittest.TestCase):

    #Tests for checking password
    def test_validate_password(self):
        valid = validate_password('Aq4@')
        self.assertEqual(valid, 'Aq4@')

    def test_validate_pass_wrong_format(self):
        valid = validate_password('Ae3')
        self.assertIn('Password format is wrong', valid)

    def test_validate_pass_empty_field(self):
        valid = validate_password('')
        self.assertIn('Please fill missing fields', valid)

    #Tests for checking username
    def test_validate_username(self):
        valid = validate_user_name('fahad2#')
        self.assertEqual(valid, 'fahad2#')

    def test_validate_username_wrong_format(self):
        valid = validate_user_name('fah')
        self.assertIn('username format is wrong', valid)

    def test_validate_username_empty_field(self):
        valid = validate_user_name('')
        self.assertIn('Please fill missing fields', valid)

    # Tests for checking email
    def test_validate_email(self):
        valid = validate_email('johndoe@mail.com')
        self.assertEqual(valid, 'johndoe@mail.com')

    def test_validate_email_empty_field(self):
        valid = validate_email('')
        self.assertIn('Please fill missing fields', valid)

    def test_validate_email_wrong_format(self):
        valid = validate_email('2johndoe2@mail.co.mhkj')
        self.assertIn('email format is wrong', valid)

    # Tests for checking name
    def test_validate_name(self):
        valid = validate_name('Denis Mab')
        self.assertEqual(valid, 'Denis Mab')

    def test_validate_name_empty_field(self):
        valid = validate_name('')
        self.assertIn('Please fill missing fields', valid)

    def test_validate_name_wrong_format(self):
        valid = validate_name('mail5co')
        self.assertIn('name format is wrong', valid)

    # Tests for checking age
    def test_check_age(self):
        valid = check_age(8)
        self.assertEqual(valid, 8)

    def test_check_age_empty_field(self):
        valid = check_age('')
        self.assertIn('Please fill missing fields', valid)

    def test_check_age_wrong_format(self):
        valid = check_age('mail5co')
        self.assertIn('age format is wrong', valid)

    def test_check_age_below_zero(self):
        valid = check_age(-12)
        self.assertEqual("Age should not be below '0'", valid)

    # Tests for checking sex
    def test_check_sex(self):
        valid = check_sex('male')
        self.assertEqual(valid, 'male')

    def test_check_sex_empty_field(self):
        valid = check_sex('')
        self.assertIn('Please fill missing fields', valid)

    def test_check_sex_wrong_format(self):
        valid = check_sex('mail5co')
        self.assertIn('sex format is wrong', valid)

