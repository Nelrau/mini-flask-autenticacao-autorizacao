from flask import render_template, Blueprint, url_for, redirect, session, request
from models.user import User
from servicos.new_user import create_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login', None)
        if not login:
            return redirect('/login')
        senha = request.form.get('senha', None)
        if not senha:
            return redirect('/login')
        
            
        user = User.query.filter_by(nome=login).first()
        print(login, user.nome)
        if not user.nome:
            create_user()
            user = User.query.first()
        if user:
            if login == user.nome and senha == user.senha:
                
                session['id_user'] = user.id
                return redirect('/perfil')
       
    
    
    return render_template('login.html')