from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField,SelectField,FileField
from wtforms.validators import InputRequired,Email,DataRequired
from flask_wtf.file import FileRequired,FileAllowed
from wtforms.widgets import TextArea


class ProfileForm(Form):
    first_name = StringField('First Name', validators = [InputRequired()])
    last_name  = StringField('Last Name', validators = [InputRequired()])
    gender     = SelectField('Gender', choices = [('Male','Male'),('Female','Female')],validators = [InputRequired()])
    location   = StringField('Location',validators=[InputRequired()])
    email      = StringField('Email Address', validators = [InputRequired(),Email()])
    biography  = TextAreaField('Biography', validators = [InputRequired()])
    image      = FileField('Profile Picture', validators=[InputRequired(),FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])