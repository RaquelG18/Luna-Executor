from glob import escape
from logging import exception
from os import abort
from flask import Flask, render_template;

#Intanciar la aplicacion
app = Flask(__name__)

#Creamos
#Controlador de la ruta ('/')
@app.route('/')

#Decorador para definir la ruta
@app.route('/index')

#Funciuon para llamar a la pagina index
def index():
    return render_template('index.html')




#Main del programa
if __name__ == '__main__':
    app.run(debug=True) #Reiniciar el servidor