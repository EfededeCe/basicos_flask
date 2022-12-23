from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField("Nombre", validators=[DataRequired(message="Complete correctamente el campo de nombre")])
    password = PasswordField("Contraseña", validators=[DataRequired(message="Ingrese su contraseña"), Length(min=4, max=16, message="Debe tener entre 4 y 16 caracteres")])
    submit = SubmitField("Enviar")
