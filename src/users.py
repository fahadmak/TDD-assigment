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


def validate_name(names):
    if not names:
        return "Please fill missing fields"
    for name in names.split(' '):
        if not name.isalpha():
            return 'name format is wrong'
    return names


def check_age(age):
    if not age:
        return "Please fill missing fields"
    if not isinstance(age, int):
        return 'age format is wrong'
    if age >= 0:
        return age
    return "Age should not be below '0'"

