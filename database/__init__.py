from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def reset_database():
	from yeyou.api.products.models import Product
	db.drop_all()
	db.create_all()