from database import db

class User (db.Model):
    id = db.Column('id',db.Integer, primary_key= True, autoincrement=True)
    nome = db.Column('nome', db.String(100))
    senha = db.Column('senha', db.String(100))
    tipo = db.Column('tipo', db.String(100))