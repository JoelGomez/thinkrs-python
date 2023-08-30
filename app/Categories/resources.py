from flask.views import MethodView
from flask import Blueprint, request

categories_bp = Blueprint('categories_bp', __name__, url_prefix='/api/')

class CategoriesList(MethodView):
    def get(self):
        return {
            {"id": 1, "name": "category 1", "description": "description 1"},
            {"id": 2, "name": "category 2", "description": "description 2"},
            {"id": 3, "name": "category 3", "description": "description 3"},
        }


class Category(MethodView):
    def get(self):
        data = request
        id = data.get('id')

        CategoriesList = {
            {"id": 1, "name": "category 1", "description": "description 1"},
            {"id": 2, "name": "category 2", "description": "description 2"},
            {"id": 3, "name": "category 3", "description": "description 3"},
        }

        return CategoriesList.index(id)


class Categories(MethodView):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        if name is None:
            return {"error": "name is required"}, 400

        if description is None:
            return {"error": "description is required"}, 400

        return {"message": "Bienvenido", "name": name, "description": description}, 201
    

categories_bp.add_url_rule(
    'categories', view_func = CategoriesList.as_view('categories_list')
)

categories_bp.add_url_rule(
    'categories', view_func = Categories.as_view('categories')
)

categories_bp.add_url_rule(
    'categories<id>', view_func = Category.as_view('category')