from flask import Blueprint, flash, render_template, url_for, request,g,redirect,flash,session,json
from bammysite import app,db,ma,mail
from bammysite.models import  Parent,Student,Siblings,subscriber,parent_schema
from bammysite.models import parents_schema,student_schema,students_schema,sibling_schema,siblings_schema,News,Admin
import os
from flask_mail import Message

sitemod = Blueprint('site', __name__, template_folder='templates')


'''# check that current users have a session
@sitemod.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']'''

@sitemod.route('/')
@sitemod.route('/index')
def index():
	return render_template('index.html')

# application
@sitemod.route('/register',methods=['GET','POST'])
def register():
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
	return render_template('register_index.html')


@sitemod.route('/admin_login',methods=['GET','POST'])
def admin_login():
	if request.method == 'POST':
		session.pop('user',None)
		email = request.form['admin-login__email']
		password = request.form['admin-login__password']
		user = Admin.query.filter_by(admin_email=email).first()
		if user != None:
			password = user.admin_password
			if request.form['admin-login__password'] == password:
				session['user'] = request.form['admin-login__email']
				return redirect(url_for('site.admin'))
			else:
				error='Password incorrect - forgot password?'
				return render_template('admin_login.html')
		else:
			error = 'No user with that email was found'
			return render_template('admin_login.html',error=error)

	return render_template('admin_login.html')

@sitemod.route('/admin')
def admin():
	if 'user' in session:
		return render_template('admin_main.html')
	return render_template('admin_login.html')

@sitemod.route('/admin_logout')
def admin_logout():
	if 'user' in session:
		session.pop('user',None)
	return redirect(url_for('site.admin_login'))

# send email
'''def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	mail.send(msg)

	return msg


@sitemod.route('/send_newsletter')
def send_newsletter():
'''

@sitemod.route('/admin_signup',methods=['GET','POST'])
def admin_signup():
	if request.method == 'POST':
		admin_email = request.form['email']
		password = request.form['password']

		admin = Admin(admin_email=admin_email,admin_password=password)
		db.session.add(admin)
		db.session.commit()
	return render_template('signup.html')
# Newsletter
@sitemod.route('/news_signup',methods=['GET','POST'])
def news_signup():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		new_subscriber = subscriber(sub_name=name,sub_email=email)
		db.session.add(new_subscriber)
		db.session.commit()

		# find parent with same details
		user = Parent.query.filter_by(email=email).first()
		if user != None:
			new_subscriber.parentid = user.id
			db.session.commit()
		else:
			try:
				user = Parent.query.filter_by(pname=name).first()
				new_subscriber.parentid = user.id
			except AttributeError:
				pass

		msg = "Congrats you've successfully registered on our mailing list"

		return render_template('index.html',msg=msg)
	return render_template('index.html')


@sitemod.route('/add_news')
def add_news():
	if request.method == 'POST':
		headline = request.form['news_headline']
		info = request.form['story-info']
		image = request.files['news_photo']

		news = News(title=headline,body=info,img_data=image.read())

		db.session.add(news)
		db.session.commit()

		news = News.query.filter_by(title=headline).first()
		if news != None:
			msg = 'News created successfully!'

	return render_template('admin_main.html',msg=msg)