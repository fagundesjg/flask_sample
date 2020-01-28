from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "Essa página não existe"}), 404


# Exemplo com query params, params e format com saida em json
@app.route("/<int:id>")  # exemplo de parametro obrigatorio com tipagem
def index(id=0):
    numero = request.args.get('id')  # query params
    # exemplo de como retornar json e formatado com variaveis
    return jsonify({"message": "Bem vindo ao python 3 {0} {1}".format(id, numero)})

# Exemplo de rota com render
@app.route("/home")
def home():
    # exemplo de como retornar um template
    return render_template("index.html", template_folder="templates")

# CTRL + SHIFT + R to refresh page with css updates


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
