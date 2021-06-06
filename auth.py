import sys
import json
from exception_practice2 import *
sys.tracebacklimit = 0
class Authenticator:
    def __init__(self, username, password, users=open('specs.json'), is_logged_in= False):
        self.username = username
        self.password = password
        self.is_logged_in = is_logged_in
        self.users = users
        self.users = self.users.read()

    def add_user(self):

        if self.username not in self.users:
            self.password = str(self.password)

            if len(self.password) >= 8:
                specs_dic = {self.username: self.password}
                file1 = open('specs.json', 'r')
                read = file1.read()
                dic = json.loads(read)
                file1.close()

                with open('specs.json', 'w') as write_file:
                    dic.update(specs_dic)
                    json.dump(dic, write_file,indent=2)

            else:
                raise PasswordTooShort
        else:
            raise UsernameAlreadyExists
    def login(self, username, password):
        file1 = open('specs.json', 'r')
        read = file1.read()
        dic = json.loads(read)
        file1.close()
        dic_keys = dic.keys()
        if username not in dic_keys:
            raise InvalidUsername
        elif username in dic_keys and dic[username] == password:

            self.is_logged_in = True
            return True

        elif username in dic_keys and dic[username] != password:
            raise InvalidPassword

        else:
            return False



    def is_log_in(self):
        if self.is_logged_in == True:

            return True
        else:

            return False


