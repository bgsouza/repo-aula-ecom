import os

class Config:
  #Vamos gerar o SECRET_KEY com: import os os.urandom(24) 
  SECRET_KEY = b'\xe4f)\xdaHL\xa3"\xba1\xac\x12_\x0fC\x1b=\xe1\xcf\xfbD\xd5\xdcQ'
  SQLALCHEMY_DATABASE_URI = "sqlite:////{path}/database.db".format(path=os.getcwd())
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
  Debug=True

class Production(Config):
  pass

conf = {
  "development": Development,
  "production": Production
}


