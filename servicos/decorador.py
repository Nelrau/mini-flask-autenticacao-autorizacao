from flask import session, redirect, g
from functools import wraps
from models.user import User

def login_required(funcao):
    @wraps(funcao)
    def verificar_login():
        if 'id_user' not in session:
            return redirect('/login')
        id = session['id_user']
        user = User.query.filter_by(id=id).first()
        g.user = user        
        return funcao()
    return verificar_login


def type_role(tipo):
    def funcaos(funcao):
        @wraps(funcao)
        def verify_role():
            if tipo == g.user.tipo:
                return funcao()
            return redirect('/perfil')
            
        return verify_role    
    return funcaos