from flask_wtf import FlaskForm 
from wtforms import DateField, StringField , PasswordField , SubmitField,EmailField,IntegerField
from wtforms.validators import DataRequired,Length,EqualTo,Email


class patint_Sign_up_Form(FlaskForm):
    
    username = StringField('User name : ', validators=[DataRequired(),Length(max=15)])
    email = StringField('Email :', validators=[DataRequired(),Length(max=50)])
    password = PasswordField('Passowrd :' , validators=[DataRequired(),Length(min=9)])
    confirm_password = PasswordField('Confirm Passowrd : ' , validators=[DataRequired(), EqualTo('password')])
    First_name = StringField('First name : ', validators=[DataRequired(),Length(max=15)])
    Last_name = StringField('Last name : ', validators=[DataRequired(),Length(max=15)])
    Age = IntegerField('Age : ', validators=[DataRequired()])
    id = IntegerField('Unique ID : ', validators=[DataRequired()])
    data_of_birth = DateField('Date of Birth : ', validators=[DataRequired()])
    disease = StringField('Disease : ', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('submit') 
    
class patient_fetch(FlaskForm):
    
    username = StringField('patient name : ', validators=[DataRequired(),Length(max=15)])
    id = IntegerField('patient ID : ', validators=[DataRequired()])
    search = SubmitField('search') 
     
class Doctor_sign_up_Form(FlaskForm):
    
    unique_id = StringField('Unique ID : ', validators=[DataRequired(),Length(max=15)])
    doctor_name = StringField('Doctor name : ', validators=[DataRequired(),Length(max=15)])
    password = PasswordField('Passowrd :' , validators=[DataRequired(),Length(min=3)])
    confirm_password = PasswordField('Confirm Passowrd : ' , validators=[DataRequired(), EqualTo('password')])
    doctor_speciality = StringField('Doctor speciality : ', validators=[DataRequired(),Length(max=50)])
    submit = SubmitField('submit')

class Doctor_sign_in_Form (FlaskForm):
    
    unique_id = StringField('Doctor ID : ', validators=[DataRequired(),Length(max=15)])
    password = PasswordField('Passowrd :' , validators=[DataRequired(),Length(min=3)])
    Login = SubmitField('Login')
