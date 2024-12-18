from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Generate and use Flask's secret key
    app.secret_key = Flask(__name__).secret_key
    
    from .routes import app_routes
    app.register_blueprint(app_routes)
    
    return app