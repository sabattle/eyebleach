from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from eyebleach.config import Config

mongo = PyMongo()
bcrypt = Bcrypt()

def create_app(config=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    print(app.config)
    mongo.cx.server_info()

    bcrypt.init_app(app)

    # Routes
    from eyebleach.main.routes import main  # noqa: E402, F401
    from eyebleach.user.routes import user  # noqa: E402, F401

    app.register_blueprint(main)
    app.register_blueprint(user)

    return app
