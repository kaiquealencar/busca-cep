from flask import Flask, render_template, request
from class_consulta_cep import ConsultaCep

app = Flask(__name__)

consulta = ConsultaCep()

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        cep = request.form.get("cep")
        resultado = consulta.consultar_cep(cep)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)