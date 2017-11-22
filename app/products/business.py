from models import Product
from database import db


def create_product(data):
	name = data.get("name")
	description = data.get("description")
	price = data.get("price")
	product = Product(name,description,price)
	db.session.add(product)
	db.session.commit()

def update_product(id, data):
	product = Product.query.get(id)
	product.name = data.get("name")
	product.description = data.get("description")
	product.price = data.get("price")
	db.session.add(product)
	db.session.commit()
	
def delete_product(id):
	product = Product.query.get(id)
	db.session.delete(product)
	db.session.commit()

def get_product(id):
	return Product.query.get(id)

def get_all_products():
	return Product.query.all()
