import unittest

from src.users import validate_password, validate_user_name, validate_email


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
        valid = validate_user_name('fahad')
        self.assertEqual(valid, 'fahad')

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
        valid = validate_email('johndoe@mail.com')
        self.assertIn('username format is wrong', valid)
