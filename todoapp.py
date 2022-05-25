from glob import escape
from logging import exception
from os import abort
from flask import Flask, render_template;

#Intanciar la aplicacion
app = Flask(__name__)

#Controlador de la ruta ('/')
@app.route('/')

#Funciuon para llamar a la pagina index
def principal():
    return render_template('index.html')



#Main del programa
if __name__ == '__main__':
    app.run(debug=True) #Reiniciar el servidor