from flask_restful import Resource, marshal, request
from app import db
from app.models import Produto
from app.schemas import produtos_fields

class Produtos(Resource):
    def get(self):
        produtos = Produto.query.all()
        return marshal(produtos, produtos_fields, "produtos")

    def post(self):
        content = request.json
        try:
            prod = Produto(content["nome"], content["descricao"], content["tipo"], content["sku"])
            db.session.add(prod)
            db.session.commit()
            return marshal(prod, produtos_fields, "produtos")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500
    
    def put(self):
        content = request.json
        prod = Produto.query.get(content["id"])
        
        if not prod:
            return {"error": "Produto não existe!"}

        try:
            prod.nome = content["nome"]
            prod.descricao = content["descricao"]
            prod.tipo = content["tipo"]
            prod.sku = content["sku"]
            db.session.add(prod)
            db.session.commit()
            return marshal(prod, produtos_fields, "produtos")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500
    
    def delete(self):
        content = request.json
        prod = Produto.query.get(content["id"])
        
        if not prod:
            return {"error": "Produto não existe!"}
        
        try:
            db.session.delete(prod)
            db.session.commit()
            return marshal(prod, produtos_fields, "produtos")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500



