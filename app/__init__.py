from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_wtf.csrf import CSRFProtect
from .config import conf
import os

# Instância do SQLAlchemy
db = SQLAlchemy()
# Habilitando o CSRF
csrf = CSRFProtect()

def create_app():
  app = Flask(__name__)
  ambiente = os.getenv('FLASK_ENV')  
  app.config.from_object(conf[ambiente])
  
  # Inicalizando nossa API
  api = Api(app, prefix="/api/v1")

  # Inicializando csrf
  csrf.init_app(app)
  
  # Bootstrap do banco
  db.init_app(app)

  from app.controller.produtos import Produtos
  api.add_resource(Produtos, "/produtos", "/produtos/<int:id>")
  
  #Formulario
  @app.route('/criar-produto')
  def form_produto():
    return render_template('produto/form.html')

  return app
