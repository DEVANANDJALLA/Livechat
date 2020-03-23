from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo
mongo = PyMongo()
socketio = SocketIO()

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'
    app.config["MONGO_URI"] = "mongodb://localhost:27017/livechat"
    mongo.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    socketio.init_app(app)
    return app

