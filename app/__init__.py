from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .config import conf
import os

# Instância do SQLAlchemy
db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  ambiente = os.getenv('FLASK_ENV')  
  app.config.from_object(conf[ambiente])
  
  # Inicalizando nossa API
  api = Api(app, prefix="/api/v1")

  # Bootstrap do banco
  db.init_app(app)

  from app.controller.produtos import Produtos
  api.add_resource(Produtos, "/produtos")
  
  return app
