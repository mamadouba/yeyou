from flask_restplus import Resource, fields
from app import api
from .business import *

ns = api.namespace('products', 'Operation related to products')
product_fields = api.model("Product", {
	"id": fields.Integer,
	"name": fields.String,
	"description": fields.String,
	"price": fields.Float
})


@ns.route('/')
class ProductList(Resource):
	
	@api.marshal_list_with(product_fields)
	def get(self):
		"""Returns a list of products"""
		return get_all_products()
	
	@api.response("201", "Product sucessfully created")
	@api.expect(product_fields, validate=True)
	def post(self):
		"""Create new product"""
		data = api.payload
		create_product(data)
		return "", 201
	
@ns.route('/<int:id>')
@api.response(404, 'Product not found')
@api.param('id', 'product ID')
class ProductItem(Resource):
	
	@api.marshal_with(product_fields)
	def get(self, id):
		"""
		Show one product details
		"""
		product = get_product(id)
		if not product:
			api.abort(404)
		return product
	
	@api.response(201, "Product successfully updated")
	@api.expect(product_fields, validate=True)
	def put(self, id):
		"""
		Update a product
		"""
		product = get_product(id)
		if not product:
			api.abort(404)
		update_product(id, api.payload)
		return "",201
	
	@api.response(204, "Product successfully deleted")
	def delete(self, id):
		"""
		Delete a product
		"""
		product = get_product(id)
		if not product:
			api.abort(404)
		delete_product(id)
		return "",204
	