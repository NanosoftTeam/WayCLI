class UserControllerClass:
    SESSION_LOGGED_IN = 0
    SESSION_USERNAME = ""
    SESSION_PASSWORD = ""

    def __init__(self):
        self.SESSION_LOGGED_IN = 0
        self.SESSION_USERNAME = ""
        self.SESSION_PASSWORD = ""

    def checkdata(self, username, password):
        # Let's assume, that data is correct, since the server is not working
        self.SESSION_USERNAME = username
        self.SESSION_PASSWORD = password
        self.SESSION_LOGGED_IN = 1
        return self.SESSION_LOGGED_IN

    def handleemail(self, lor: str):
        if lor == 'l':
            # if login
            return
        else:
            # if register
            return
        return

    def handlepassword(self, lor: str):
        if lor == 'l':
            # if login
            return
        else:
            # if register
            return
        return

    def handlerepeatpassword(self):
        return