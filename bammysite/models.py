from bammysite import db,ma

class H_User(db.Model):
	# Ward's details
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	Sname = db.Column(db.String(100))	
	Sdate = db.Column(db.String(200))
	Sbg = db.Column(db.String(100))
	Sbp = db.Column(db.String(100))
	Sog = db.Column(db.String(50))
	Sgen = db.Column(db.String(50))
	Slga = db.Column(db.String(50))

	# prospective student's details
	Ssch = db.Column(db.Text(200))
	Sscha = db.Column(db.String(200))
	Sclass = db.Column(db.String(100))
	Syear = db.Column(db.String(100))

	# Parent's details
	name = db.Column(db.String(100))
	raddress = db.Column(db.String(100))
	oaddress = db.Column(db.String(100))
	tel = db.Column(db.String(100))
	email = db.Column(db.String(100))
	family = db.Column(db.String(100))
	siblings = db.Column(db.Integer)

	#relationship
	children = db.relationship('h_user_ow',backref='parent')

# sibling class
class H_User_ow(db.Model):
	id = db.Column(db.Integer,nullable=False,primary_key=True)
	name = db.Column(db.String(100))
	sibclass = db.Column(db.String(100))
	sibyear = db.Column(db.String(100))
	parentid = db.Column(db.Integer,db.ForeignKey('h_user.id'))


# User Schema
class UserSchema(ma.Schema):
	class Meta:
		fields = ('id','name','email','password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Note Schema
class NoteSchema(ma.Schema):
	class Meta:
		fields = ('id','title','body')

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)