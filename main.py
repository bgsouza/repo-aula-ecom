from app import create_app, db
from flask_migrate import Migrate
from app.models import Produto

app = create_app()
Migrate(app, db)

# Opcional: Habilitando modo iterativo: flask shell
@app.shell_context_processor
def shell_context():
  return dict(
    app=app,
    db=db    
  )

# chamado manualmente com: $ flask run
if __name__ == "__main__":
  app.run()

# Lembrar de exeutar 
# FLASK_APP=run.py
# FLASK_ENV