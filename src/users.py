from src.model import users, User
from src.helpers import validate_password, validate_email, validate_user_name, validate_name, \
    check_sex, check_age, search_user_by_name
# 400 - means  fill in correct information
# 401 - Missing fields


def create_user(name, username, age, email, password, gender):
    valid_name = validate_name(name)
    valid_username = validate_user_name(username)
    valid_age = check_age(age)
    valid_email = validate_email(email)
    valid_password = validate_password(password)
    valid_sex = check_sex(gender)
    if 400 in [valid_name, valid_sex, valid_username, valid_password, valid_email, valid_age]:
        return "Please fill in the correct information"
    if 401 in [valid_name, valid_sex, valid_username, valid_password, valid_email, valid_age]:
        return "Please fill in the missing fields"
    if valid_name == valid_username:
        return "username should not be the  same as the name"
    user_name = search_user_by_name(username)
    if user_name:
        return "The User name already exists"
    user_id = max([user.to_dict().get('user_id') for user in users]) + 1 if users else 1
    user = User(user_id, name, username, age, email, password, gender)
    users.append(user)
    return "{user.name} user has been created ".format(user=user)


