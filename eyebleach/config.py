import os

class Config:
    SECRET_KEY = os.environ.get('EYEBLEACH_SECRET_KEY')
    MONGO_URI = "mongodb://localhost:27017/eyebleach"
