selections = {
            '1': 'Register User',
            '2': 'Log In',
            '3': 'Log out',
            '4': 'Exit'
            }

login_otions = {
            '1': 'Edit User',
            '2': 'View Profile',
            }


def main_options():
    for k, v in selections.items():
        print("{}. {}".format(k, v))
    return


def login_options():
    for k, v in selections.items():
        print("{}. {}".format(k, v))