from flask import Flask, redirect

# para levantar el servidor podemos instalar la libreria python-dotenv,
# creamos el archivo .env y en el las variables de entorno necesarias
# para que simplemente corramos en terminal " flask run "
# de esta forma no es necesario poner el "if __name__(...)"

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Hola flask</h1>
    """

@app.route('/usuario/')
@app.route('/usuario/<string:name>')
@app.route('/usuario/<string:name>/<int:id>')
def user(name=None, id=None):
    if name is not None:
        if id is not None:
            return f'Hola {name}, su id es {id}'
        return f'Hola {name}'
    else:
        return 'Hola, por favor registrese'

@app.route('/login/')
@app.route('/login/<name>')
def login(name=None):
    if name is not None:
        return redirect(f"/usuario/{name}")
    else:
        return "<h1>Ingrese su nombre</h1>"

        


# if __name__ == "__main__":
#     app.run(debug=True)
