from flask import Flask
from .db import mysql
from .config import Config
def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    mysql.init_app(app)
    from .routes.cart_route import cart_bp
    app.register_blueprint(cart_bp)
    return app

