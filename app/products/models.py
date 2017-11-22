from database import db

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	description = db.Column(db.String)
	price = db.Column(db.Float)
	
	def __init__(self,name, description, price):
		self.name = name
		self.description = description
		self.price = price
		
	def __repr__(self):
		return '<Products %r>' % self.name