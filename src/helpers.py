import re

from src.model import users, User

def validate_password(password):
    if not password:
        return 401
    if isinstance(password, int):
        return 400
    if re.match(re.compile(r'([A-Z][a-z][0-9][!@#$%&*])'), password):
        return password
    return 400


def validate_user_name(user_name):
    if not user_name:
        return 401
    if isinstance(user_name, int):
        return 400
    if re.match(re.compile(r'([a-z]{4,10})'), user_name):
        return user_name
    return 400


def validate_email(email):
    if not email:
        return 401
    if isinstance(email, int):
        return 400
    if re.match(re.compile(r'[a-z-]+@[^.].*\.[a-z]{2,10}$'), email):
        return email
    return 400


def validate_name(names):
    if not names:
        return 401
    if isinstance(names, int):
        return 400
    for name in names.split(' '):
        if not name.isalpha():
            return 400
    return names


def check_age(age):
    if not age:
        return 401
    if not isinstance(age, int):
        return 400
    if age >= 0:
        return age
    return 400


def check_sex(sex):
    if not sex:
        return 401
    if sex in ['male', 'female']:
        return sex
    return 400


def search_user_by_name(user_name):
    if not users:
        return 0
    for user in users:
        if user_name is user.username:
            return user
    return 0

def match_name_password(name, password):
    if not users:
        return 0
    for user in users:
        if name == user.name and password == user.password:
            return user
    return 0

