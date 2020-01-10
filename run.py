from flask_migrate import Migrate
from flask import render_template
from bammysite import __call__,db
import os

app = __call__(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app,db)