'''Modulo para la creacion de formularios'''
from wtforms import Form
from wtforms import RadioField
from wtforms import StringField
from wtforms import EmailField
from wtforms import SelectField

class  UserForm(Form):
    '''Formulario para el registro de usuarios'''
    nombre = StringField('Nombre')
    apellido = StringField('Apellido')
    email = EmailField('Email')
    materias = SelectField(choices=[('Espanol','Esp'), ('Matematicas','Mat'), ('Ingles','Ing')])
    radios = RadioField('Curso', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')])
