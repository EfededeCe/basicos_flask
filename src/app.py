from flask import Flask, redirect, url_for, request, render_template

# para levantar el servidor podemos instalar la libreria python-dotenv,
# creamos el archivo .env y en el las variables de entorno necesarias
# para que simplemente corramos en terminal " flask run "
# de esta forma no es necesario poner el "if __name__(...)"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

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
            return redirect(url_for("dashboard", name=username))
    else:
        return render_template("login.html")


@app.route('/profile/')
@app.route('/profile/<string:name>')
def dashboard(name=None):
    if name is not None:
        return render_template("dashboard.html", name=name)
    else:
        return redirect(url_for("login"))



# if __name__ == "__main__":
#     app.run(debug=True)
