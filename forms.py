'''Modulo para la creacion de formularios'''
from wtforms import Form, RadioField, StringField, validators, EmailField, SelectField

class  UserForm(Form):
    '''Formulario para el registro de usuarios'''
    nombre = StringField('Nombre', [validators.Length(min=1, max=50)])
    apellido = StringField('Apellido', [validators.Length(min=1, max=50)])
    email = EmailField('Email', [validators.Length(min=6, max=50)])
    materias = SelectField(choices=[('Espanol','Esp'), ('Matematicas','Mat'), ('Ingles','Ing')])
    radios = RadioField('Curso', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6')])
