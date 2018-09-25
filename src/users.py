import re


def validate_password(password):
    if not password:
        return "Please fill missing password"
    if re.match(re.compile(r'([A-Z][a-z][0-9][!@#$%&*]$)'), password):
        return password
    return 'Password format is wrong'

