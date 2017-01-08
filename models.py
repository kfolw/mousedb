from app import db
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship 

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


class Log(db.Model):
	__tablename__ = "logentry"

	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.DateTime())
	note = db.Column(db.String())
	mouse_id = db.Column(db.Integer, ForeignKey('mouse.id'))

	owner = relationship("Mouse", back_populates="logs")

	def __init__(self, date, note):
		self.date = date
		self.note = note

	def __repr__(self):
		return '<id {}>'.format(self.id)

Mouse.logs = relationship("Log", order_by="Log.id", back_populates="owner")