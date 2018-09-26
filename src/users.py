from src.model import users, User
from src.helpers import validate_password, validate_email, validate_user_name, validate_name, \
    check_sex, check_age, search_user_by_name, match_name_password
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
    user_id = max([user.user_id for user in users]) + 1 if users else 1
    user = User(user_id, name, username, age, email, password, gender)
    users.append(user)
    return "{user.name} user has been created".format(user=user)


def login(user_name, password):
    valid_username = validate_user_name(user_name)
    valid_password = validate_password(password)
    if 400 in [valid_username, valid_password]:
        return "Please fill in the correct information"
    if 401 in [valid_username, valid_password]:
        return "Please fill in the missing fields"
    for user in users:
        if user_name == user.username and password == user.password:
            user.is_logged_in()
            print("You are Logged in")
            return user
    return "username and password do not match"


def edit_user(user_name, password, new_user_name, new_password):
    new_username = validate_user_name(new_user_name)
    new_password = validate_password(new_password)
    if 400 in [new_username, new_password]:
        return "Please fill in the correct information"
    if 401 in [new_username, new_password]:
        return "Please fill in the missing fields"
    user = login(user_name, password)
    if not isinstance(user, User):
        return "you must be logged in to edit your information"
    for user in users:
        user.username = new_user_name
        user.password = new_password
        return "User has succesfully edited his username and password"


