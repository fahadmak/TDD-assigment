users = []
class User:
    """
        A class used to represent a User

        ...

        Attributes
        ----------
        user_id : int
            the id number of the user
        name : str
            the name of the user
        username : str
            the username of the user
        age : int
            the age of the user
        email : str
            the email of user
        password : str
            the password of the user
        gender : str
            the gender of user
        status : bool
            the status of activity of user

        Methods
        -------
        __str__(self)
            Prints the user's name, username and age
        to_dict(self)
            converts a user object to dictionary format
        """

    def __init__(self, user_id, name, username, age, email, password, gender):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.age = age
        self.email = email
        self.password = password
        self.gender = gender
        self.status = False

    def __str__(self):
        """A method that Prints the user's name, username and age"""
        return "User's {0}, {1} and {2}".format(self.name, self.username, self.age)

    def to_dict(self):
        """A method that converts a user object to dictionary format"""
        user = {
            'user_id': self.user_id,
            'name': self.name,
            'username': self.username,
            'age': self.age,
            'email': self.email,
            'password': self.password,
            'gender': self.gender,
            'active': self.status
        }

        return user

    def is_logged_in(self):
        self.status = True

