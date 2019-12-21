from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_mail import Mail
import os

app = Flask(__name__)
'''basedir = os.path.abspath(os.path.dirname(__file__))

# session key
#app.secret_key = os.urandom(24)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bammy.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False'''

app.config.from_envvar('APP_SETTINGS')

# Init db
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Init flask-mail
mail = Mail(app)

# session key
app.secret_key = os.urandom(24)

# import blueprint
from bammysite.site.views import sitemod

# register blueprint
app.register_blueprint(site.views.sitemod)