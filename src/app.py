from flask import Flask, redirect, url_for, request

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

@app.route('/login/', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username and password:
            return redirect(url_for("user", name=username))
    else:
        return """<h1>Ingrese su nombre y contraseña</h1>
        <form method="POST">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="Enviar">
        </form>"""



# if __name__ == "__main__":
#     app.run(debug=True)
