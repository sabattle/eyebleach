from datetime import datetime
from eyebleach import mongo

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.register_date = datetime.utcnow()

    def register(self):
        # Insert user into MongoDB
        pass
