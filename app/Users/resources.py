from flask.views import MethodView
from flask import Blueprint, request
users_bp = Blueprint('users_bp', __name__, url_prefix='/api/')

class UserList(MethodView):
    def get(self):
        return {"username": "Joel", "email":"joel.lgr@gmail.com"}

class UsersId(MethodView):
    def get(self, id):
        return {"id": id, "username": "usuario"}
    
class Users(MethodView):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')

        if email is None:
            return {"error": "email is required"}, 400
        
        if username is None:
            return {"error": "username is required"}, 400
        
        return {"message": "Bienvenido", "email": email, "username": username}, 201


users_bp.add_url_rule(
    'users', view_func = UserList.as_view('users_list')
)

users_bp.add_url_rule(
    'users', view_func = Users.as_view('users')
)

users_bp.add_url_rule(
    'users<user_id>', view_func = UsersId.as_view('users_id')
        