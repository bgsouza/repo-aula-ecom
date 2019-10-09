from app import db

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(35), nullable=False)
    descricao = db.Column(db.String(1000), nullable=True)
    tipo = db.Column(db.String(15), nullable=False )
    sku = db.Column(db.String(35), nullable=True )

    def __init__(self, nome, descricao, tipo, sku):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.sku = sku
    
    def __repr__(self):
        return f"<Produto: {self.tipo}"

        