from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import conf
import os

# Instância do SQLAlchemy
db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  ambiente = os.getenv('FLASK_ENV')  
  app.config.from_object(conf[ambiente])
  # Bootstrap do banco
  db.init_app(app)
  
  return app
