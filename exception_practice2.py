class AuthException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Error Is {self.message}'
        else:
            return 'AuthException'
class UsernameAlreadyExists(AuthException):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Error Is {self.message}'
        else:

            return 'Username Already Exists! Please Choose Another UserName'

class PasswordTooShort(AuthException):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    def __str__(self):
        if self.message:
            return f'Error Is {self.message}'
        else:

            return 'Your Password Most More Than 8 Character.'

class InvalidUsername(AuthException):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Error Is {self.message}'
        else:

            return 'Invalid Username'

class InvalidPassword(AuthException):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Error Is {self.message}'
        else:

            return 'Invalid Password'

