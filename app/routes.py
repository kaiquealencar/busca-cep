from flask import Blueprint, render_template, request
from .class_consulta_cep import ConsultaCep

bp = Blueprint("main", __name__)

consulta = ConsultaCep()

@bp.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    
    if request.method == "POST":
        cep = request.form.get("cep")
        resultado = consulta.consultar_cep(cep)
    
    return render_template("index.html", resultado=resultado)
