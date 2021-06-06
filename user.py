from auth import *
from exception_practice2 import *

class User(Authenticator):
    def __init__(self, username, password):
        super().__init__(username, password)

    def check_login(self):
        if self.is_log_in():
            print(f"{self.username} Is Logged In")
            return True

        elif self.is_log_in() == False :
            print(f"{self.username} Is Not Logged In")
            return False

        else:
            raise AuthException









