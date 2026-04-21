from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = ["Ana", "Betto", "Carla"]

@app.route("/usuarios")
def obtener_usuarios():
    return {"lista_usuarios": usuarios}



@app.route('/buzon', methods=['GET', 'POST'])
def buzon():
    if request.method == 'GET':
        return "Este es el formulario. Usa POST para enviar datos."

    if request.method == 'POST':
        # Sacamos los datos que enviaste
        nombre = request.json['nombre']
        return f"Hola {nombre}, recibí tu formulario"


@app.route("/")
def index():
    return render_template('index.html')

    
if __name__ == "__main__":
    app.run(debug=True)