import re


def validate_password(password):
    if not password:
        return "Please fill missing fields"
    if re.match(re.compile(r'([A-Z][a-z][0-9][!@#$%&*])'), password):
        return password
    return 'Password format is wrong'


def validate_user_name(user_name):
    if not user_name:
        return "Please fill missing fields"
    if re.match(re.compile(r'([a-z]{4,10})'), user_name):
        return user_name
    return 'username format is wrong'

def validate_email(email):
    if not email:
        return "Please fill missing fields"
    if re.match(re.compile(r'[a-z-]+@[^.].*\.[a-z]{2,10}$'), email):
        return email
    return 'email format is wrong'