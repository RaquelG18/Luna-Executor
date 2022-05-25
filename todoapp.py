
from flask import Flask, render_template_string
from flask import render_template

# Intanciar la aplicacion
app = Flask(__name__, template_folder='template')

# Creamos
# Controlador de la ruta ('/')


@app.route('/')
# Función para llamar a la página index
def index():
    return render_template("index.html")

# @app.route('/enviar')
# def enviar_form():

# Controlador enviar
# @app.route('/enviar')
# def enviar_form():


# Controlador borrar
# @app.route('/borrar')
# def borrar_form():


# Main del programa
# if __name__ == '__main__':
app.run(debug=True)  # Reiniciar el servidor
