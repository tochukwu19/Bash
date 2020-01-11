from flask import Flask,render_template
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
    from bammysite.site import sitemod

    app.register_blueprint(sitemod)

    app.secret_key = os.urandom(24)

    '''with app.app_context():
                	def send_email(subject='',sender=app.config['MAIL_DEFAULT_SENDER'],recipients=[],text_body=render_template('newsletter.txt'),html_body=render_template('newsletter.html')):
                		msg = Message(subject=subject,sender=sender,recipients=recipients)
                		msg.body = text_body
                		msg.html = html_body
            
                	def send_mail(subject='',sender=app.config['MAIL_DEFAULT_SENDER'],recipients=[],text_body=render_template('newsletter.txt'),html_body=render_template('newsletter.html')):
                		msg = Message(subject=subject,sender=sender,recipients=recipients)
                		msg.body = text_body
                		msg.html = html_body
                		mail.send(msg)
            
                	def send_batch(data):
                		with mail.connect() as conn:
                			for user in data['recipients']:
                				send_email(**data)
            
                				conn.send(msg)'''

    return app