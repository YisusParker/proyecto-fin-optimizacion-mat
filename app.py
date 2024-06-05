from flask import Flask, render_template, request, jsonify
from optimizer import (
    plan_entrenamiento,
)  # Importar la función de optimización desde el módulo optimizer

# Crear una instancia de la aplicación Flask
app = Flask(__name__)


# Definir la ruta para la página de inicio
@app.route("/")
def index():
    # Renderizar la plantilla index.html cuando se acceda a la ruta raíz
    return render_template("index.html")


# Definir la ruta para la página principal
@app.route("/main")
def main():
    # Renderizar la plantilla main.html cuando se acceda a la ruta /main
    return render_template("main.html")


# Definir la ruta para la optimización, permitiendo solo métodos POST
@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        # Obtener el número de días del formulario enviado y convertirlo a entero
        num_dias = int(request.form["dias"])
        # Verificar que el número de días esté dentro del rango permitido
        if num_dias < 3 or num_dias > 7:
            return jsonify(
                {"error": "Por favor, ingrese un número válido entre 3 y 7."}
            )
    except ValueError:
        # Manejar el caso en que el valor ingresado no sea un número entero válido
        return jsonify({"error": "Por favor, ingrese un número válido entre 3 y 7."})

    # Llamar a la función de optimización con el número de días ingresado
    resultado, valor_optimo = plan_entrenamiento(num_dias)
    # Devolver el resultado y el valor óptimo en formato JSON
    return jsonify({"resultado": resultado, "valor_optimo": valor_optimo})


# Ejecutar la aplicación en modo de depuración si este script es ejecutado directamente
if __name__ == "__main__":
    app.run(debug=True)
