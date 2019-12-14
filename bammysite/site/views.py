from flask import Blueprint, render_template, url_for, request,g,redirect,flash,session,json
from bammysite import db, ma,app
from bammysite.models import  Parent,Student,Siblings,parent_schema,parents_schema,student_schema,students_schema,sibling_schema,siblings_schema
import os

sitemod = Blueprint('site', __name__, template_folder='templates')


'''# check that current users have a session
@sitemod.before_request
def before_request():
	g.user = None
	if 'user' in session:
		g.user = session['user']'''


# High school application
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

		# fetch sibling data
		s_name = request.json['s_name']
		s_class = request.json['s_class']
		s_year = request.json['s_year']

