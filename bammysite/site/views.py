from flask import Blueprint, render_template, url_for, request,g,redirect,flash,session,json
from bammysite import app,db,ma,mail
from bammysite.models import  Parent,Student,Siblings,parent_schema,parents_schema,student_schema,students_schema,sibling_schema,siblings_schema
import os
from flask_mail import Message

sitemod = Blueprint('site', __name__, template_folder='templates')


'''# check that current users have a session
@sitemod.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']'''


# send email
def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)

# Newsletter
@sitemod.route('/new_signup',methods=['GET','POST'])
def news_signup():
	name = request.name['name']
	email = request.form['email']

	

# application
@sitemod.route('/application',methods=['GET','POST'])
def application():
	if request.method == 'POST':
		# fetch parent-data from form
		pname = request.json['name']
		raddress = request.json['raddress']
		oaddress = request.json['oaddress']
		tel = request.json['tel']
		email = request.json['email']
		family = request.json['family']
		etel = request.json['Etel']
		siblings = reuest.json['siblings']
		
		# fetch student data
		sname = request.json['sname']
		dob = request.json['dob']
		bg = request.json['bg']
		bp = request.json['bp']
		state = request.json['state']
		gen = request.json['gen']
		lga = request.json['lga']
		school = request.json['school']
		school_address = request.json['school_address']
		class_ = request.json['class_']
		year = request.json['year']
		sex = request.json['sex']
		ail = srequest.json['ail']

		# fetch sibling data
		s_name = request.json['s_name']
		s_class = request.json['s_class']
		s_year = request.json['s_year']

		# create parent object
		parent = Parent(pname=pname,raddress=raddress,oaddress=oaddress,tel=tel,email=email,family=family,etel=etel,siblings=siblings)

		# Student object
		student = Student(sname=sname,dob=dob,bg=bg,bp=bp,state=state,gen=gen,lga=lga,sex=sex,ail=ail,school=school,school_address=school_address,class_=class_,year=year)

		# Sibling object
		sibling = Sibling(s_name=s_name,s_class_=s_class,s_year=s_year)

		db.session.add_all([parent,student,sibling])

		db.commit()

		# parse data
		return render_template("pay.html")