from flask_restful import fields

produtos_fields = {
    "id": fields.Integer,
    "nome": fields.String,
    "descricao": fields.String,
    "tipo": fields.String,
    "sku": fields.String,
}

