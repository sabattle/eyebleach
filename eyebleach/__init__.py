from flask import Flask
import os

app = Flask(__name__)

# Get key
app.config['SECRET_KEY'] = os.environ['EYEBLEACH_SECRET_KEY']

from eyebleach import routes  # noqa: E402, F401
