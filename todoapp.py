
from flask import Flask, request, redirect, url_for
from flask import render_template

# Intanciar la aplicacion
app = Flask(__name__, template_folder='template')

# Creamos
# Controlador de la ruta ('/')


@app.route('/')
# Función para llamar a la página index
def index():
    return render_template("index.html")


@app.route('/enviar')
def enviar():
    return render_template("index.html")

    # Controlador borrar
@app.route('/borrar/<tareas>')
def borrar_form(tareas):
    return render_template('index.html')

        # Main del programa
        # if __name__ == '__main__':

app.run(debug=True)  # Reiniciar el servidor

