from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_mail import Mail,Message
from flask_script import Manager
from config import config
import os

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
manager = Manager()

def __call__(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    # register blueprint
    from bammysite.site.views import sitemod as bash

    app.register_blueprint(bash)

    app.secret_key = os.urandom(24)

    return app