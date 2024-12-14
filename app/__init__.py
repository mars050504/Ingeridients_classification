from flask import Flask
from flasgger import Swagger

def create_app():
  app = Flask(__name__)
  
  # Initialize Swagger
  swagger = Swagger(app)
  
  with app.app_context():
    from app.routes import api
    app.register_blueprint(api, url_prefix="/api") # use /api prefix for rest api routes
    
    return app