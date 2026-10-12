from flask import Flask, render_template
from models.user import User
from database import db
from servicos.decorador import login_required
from routes.login import login_bp
from routes.logout import logout_bp
from routes.perfil import perfil_bp
from routes.motorista import motorista_bp
from routes.adm import adm_bp


app = Flask(__name__)
app.secret_key= 'lsfjçs'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mini_autenticacacao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(perfil_bp)
app.register_blueprint(motorista_bp)
app.register_blueprint(adm_bp)


@app.route('/')
@login_required
def index():
    return render_template('index.html')

if not User:
    with app.app_context():
        from models.user import User
    #     from models.curso import Curso
    #     from models.matricula import Matricula

        db.create_all()


if __name__ == '__main__':
    app.run(debug=True)