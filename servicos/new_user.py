from models.user import User
from database import db
def create_user():
    usuario = User.query.filter_by(nome='pedro').first()
    print(usuario.nome if usuario else 'Pedro não encontrado')
    if not usuario:
        user = User(nome='pedro', senha='300018', tipo='motorista')
        db.session.add(user)
        db.session.commit()
    else:
        print(usuario)