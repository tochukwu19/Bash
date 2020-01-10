'''from flask_mail import Message
from ..models import subscriber
from flask import render_template

# fetch all subscribers
#users = subscriber.query.all()

# single email
def send_email(subject='', sender=app.config['MAIL_DEFAULT_SENDER'], recipients=[], text_body=render_template('newsletter.txt'), html_body=render_template('newsletter.html'),*args,**kwargs):
	msg = Message(subject=subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	#mail.send(msg)

# bulk email
def send_batch(data):
	with mail.connect() as conn:
		for user in data['recipients']:
			send_email(**data)

			conn.send(msg)	
'''