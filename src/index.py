# Importar la biblioteca Flask del entorno flask
from flask import Flask, render_template
# Inicializar Flask obteniendo un objeto para manejar la aplicación web
app = Flask(__name__)
# Crear rutas utilizando decoradores


@app.route('/')
def inicio():
    return render_template('home.html')


@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')


@app.route('/param/<string:nombre>')
def parametros(nombre):
    ies = "Palomeras-Vallecas"
    usuario = {
        "nombre": "Juan",
        "apellidos": "García González",
        "edad": 21
    }
    lista_usuarios = [
        {
            "nombre": "Juan",
            "apellidos": "García González",
            "edad": 21
        },
        {
            "nombre": "Ana",
            "apellidos": "Jiménez Fernández",
            "edad": 20
        },
        {
            "nombre": "Helen",
            "apellidos": "Smith",
            "edad": 19
        },
    ]

    return render_template('param.html', nombre=nombre, centro=ies, usu=usuario, lista_usu=lista_usuarios)


# Hacemos que aplicación se mantenga a la escucha de peticiones web
# comprobando primero si estamos en el archivo principal (__main__)
if __name__ == '__main__':
    app.run(debug=True)
