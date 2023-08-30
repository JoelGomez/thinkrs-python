from flask import Flask
from flask.views import MethodView

from .Users.resources import users_bp
from .Categories.resources import categories_bp

class HelloWorld(MethodView):
    def get(self):
        return {"message": "Hello World"}
    

def create_app():
    app = Flask(__name__)

    HelloWorld = HelloWorld.as_view('hello_world')

    app.add_url_rule('/', view_func = HelloWorld)
    app.add_url_rule('/api/', view_func = HelloWorld)
    app.register_blueprint(users_bp)
    app.register_blueprint(categories_bp)

    return app