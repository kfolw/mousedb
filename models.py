from app import db
from sqlalchemy.dialects.postgresql import JSON


class Mouse(db.Model):
	__tablename__ = 'mouse'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	genotype = db.Column(db.String())

	def __init__(self, name, genotype):
		self.name = name
		self.genotype = genotype

	def  __repr__(self):
		return '<id {}>'.format(self.id)