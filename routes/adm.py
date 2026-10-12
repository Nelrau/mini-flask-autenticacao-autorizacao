from flask import Blueprint
from servicos.decorador import login_required, type_role

adm_bp = Blueprint('adm', __name__)

@adm_bp.route('/adm', methods=['GET', 'POST'])
@login_required
@type_role('adm')
def adm():
    return '''<h2>pagina adm</h2>
<a href="/">Home</a>'''