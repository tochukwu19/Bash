from bammysite import db,ma

# Parent's data
class Parent(db.Model):
	# Parent's details
	__tablename__ = 'Parent'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	name = db.Column(db.String(100))
	raddress = db.Column(db.String(100))
	oaddress = db.Column(db.String(100))
	tel = db.Column(db.String(100))
	email = db.Column(db.String(100))
	family = db.Column(db.String(100))
	siblings = db.Column(db.Integer)

	#relationship
	children = db.relationship('Siblings','Student',backref='parent')

# Model below describes prospective student's data

class Student(db.Model):
	# Ward's details
	__tablename__ = 'Student'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	name = db.Column(db.String(100))	
	dob = db.Column(db.String(200))
	bg = db.Column(db.String(100))
	bp = db.Column(db.String(100))
	state = db.Column(db.String(50))
	gen = db.Column(db.String(50))
	lga = db.Column(db.String(50))

	school = db.Column(db.Text(200))
	school_address = db.Column(db.String(200))
	class_ = db.Column(db.String(100))
	year = db.Column(db.String(100))
	parentid = db.Column(db.Integer,db.ForeignKey('Parent.id'))

# sibling details
class Siblings(db.Model):
	__tablename__ = 'Siblings'
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	name = db.Column(db.String(100))
	class_ = db.Column(db.String(100))
	year = db.Column(db.String(100))
	parentid = db.Column(db.Integer,db.ForeignKey('Parent.id'))

# Parent's Serialization Schema
class ParentSchema(ma.Schema):
	class Meta:
		fields = ('id','name','email','tel','family','siblings','oaddress','raddress')

parent_schema = ParentSchema()
parents_schema = ParentSchema(many=True)

# Student's Serialization Schema
class StudentSchema(ma.Schema):
	class Meta:
		fields = ('id','name','dob','bg','bp','state','gen','lga','school','school_address','class_','year','parentid')

student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

# sibling schema
class SiblingSchema(ma.Schema):
	class Meta:
		fields = ('id','name','class_','year','parentid')

sibling_schema = SiblingSchema()
siblings_schema = SiblingSchema(many=True)