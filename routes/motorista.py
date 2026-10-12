from flask import Blueprint, render_template, g
from servicos.decorador import login_required, type_role

motorista_bp = Blueprint('motorista', __name__)

@motorista_bp.route('/motorista', methods=['GET', 'POST'])
@login_required
@type_role('motorista')
def motorista():
    return '''<h2>Motorista</h2>
<a href="/">Home</a>'''