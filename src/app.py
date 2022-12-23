from flask import Flask, redirect, url_for, request, render_template,\
    flash, session
from forms import LoginForm
# para levantar el servidor podemos instalar la libreria python-dotenv,
# creamos el archivo .env y en el las variables de entorno necesarias
# para que simplemente corramos en terminal " flask run "
# de esta forma no es necesario poner el "if __name__(...)"

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secreta!!"  # se usa para enviar los msg de flash 


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
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        username = form.username.data
        password = form.password.data
        if username and password:
            session["username"] = username
            return redirect(url_for("dashboard", name=username))
        flash("Ingresa los datos correctamente.", "error") # envía msg y categoría
    return render_template("login.html", form=form)

    # Así funciona sin el validador csfr de wtform, que da un token
    # form = LoginForm()
    # if form.validate_on_submit() and request.method == "POST":
    #     username = request.form["username"]
    #     password = request.form["password"]
    #     if username and password:
    #         session["username"] = username
    #         return redirect(url_for("dashboard", name=username))
    #     flash("Ingresa los datos correctamente.", "error") # envía msg y categoría
    # return render_template("login.html", form=form)

def new_func():
    return "error"


@app.route('/profile/')
@app.route('/profile/<string:name>')
def dashboard(name=None):
    if name is not None:
        flash(f"Bienvenidx {name}","success")
        return render_template("dashboard.html", name=name)
    return redirect(url_for("login"))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))


# if __name__ == "__main__":
#     app.run(debug=True)
