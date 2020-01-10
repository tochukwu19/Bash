from flask_migrate import Migrate
from flask import render_template
from bammysite import __call__,db
import os

app = __call__(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app,db)

with app.app_context():
	def send_email(subject='',sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[], text_body=render_template('newsletter.txt'), html_body=render_template('newsletter.html'),*args,**kwargs):
		msg = Message(subject=subject,sender=sender,recipients=recipients)
		msg.body = text_body
		msg.html = html_body

	def send_batch(data):
		with mail.connect() as conn:
			for use in data['recipients']:
				send_email(**data)
				conn.send(msg)
