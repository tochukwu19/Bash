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

