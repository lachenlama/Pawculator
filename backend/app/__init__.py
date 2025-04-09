from flask import Flask
from app.routes import routes as bp

def create_app():
    app = Flask(__name__, 
               template_folder='../templates',
               static_folder='../static')
    app.register_blueprint(bp)
    return app
