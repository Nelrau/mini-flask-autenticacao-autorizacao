from flask import Blueprint, render_template, url_for
from servicos.decorador import login_required

perfil_bp = Blueprint('perfil', __name__)

@perfil_bp.route('/perfil', methods=['GET','POST'])
@login_required
def perfil():
    return render_template('perfil.html')