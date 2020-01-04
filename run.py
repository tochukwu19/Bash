from bammysite import app,db
from flask_migrate import Migrate

# flask-migrate
migrate = Migrate(app,db)
