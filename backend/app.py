from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def comparar_rostros(bytes_1, bytes_2):
    # Aquí iría la lógica para comparar los rostros
    # Esta función debería devolver el resultado de la comparación
    # Por ahora, solo devolveremos un mensaje de prueba
    return "¡Endpoint para comparar rostros!"

@app.route('/')
def index():
    return '¡Bienvenido al servidor de comparación de rostros!'

@app.route('/compare-faces', methods=['POST'])
def compare_faces():
    image1 = request.files['image1'].read()
    image2 = request.files['image2'].read()

    result = comparar_rostros(image1, image2)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
