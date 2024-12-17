from flask import Flask, flash, jsonify, redirect, render_template, request, send_file, session, url_for , make_response
from flask_wtf import FlaskForm
from forms import  patint_Sign_up_Form , Doctor_sign_up_Form , Doctor_sign_in_Form , patient_fetch
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate


DATABASE_URL='sqlite:///Clinc.db'

app = Flask(__name__)

app.config['SECRET_KEY']='1234567'
app.config["SQLALCHEMY_DATABASE_URI"]=DATABASE_URL
db=SQLAlchemy(app)
migrate = Migrate(app, db)

#doctor tabel
class doctor(db.Model):
    __tablename__="doctor"
    unique_id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    doctor_speciality = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
       return f'<Doctor {self.doctor_name}>'

#doctor patient
class patient(db.Model):
    __tablename__="patient"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    First_name = db.Column(db.String(15), nullable=False)
    Last_name = db.Column(db.String(15), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    data_of_birth = db.Column(db.Date, nullable=False)
    disease = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<{self.id}:{self.username}>'

#many to many relationship table
class patient_doctor(db.Model):
    __tablename__="patient_doctor"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.unique_id'), nullable=False)
    def __repr__(self):
         return f'<PatientDoctor id={self.id} patient_id={self.patient_id} doctor_id={self.doctor_id}>'


with app.app_context():
    db.create_all()

# home page
@app.route('/', methods=['GET', 'POST'])
def home ():
    return render_template('home.html', title ='Clinic Application')

#page to swip between doctor futures
@app.route('/swip', methods=['GET', 'POST'])
def swip ():
    return render_template('swip.html', title ='Clinic Application')

# search for sapcfic patient wich asigend to the doctor user
@app.route('/patient_fetch', methods=['GET', 'POST'])
def patient_fetch_cl():
    form = patient_fetch()
    doctor_id = session.get('unique_id')
    if request.method == "GET":
        return render_template('patint_fetch.html', title='Clinic Application', form=form, patient=None)

    elif request.method == 'POST' and form.validate_on_submit():
      id = form.id.data
      username = form.username.data  
        
        # Fetch the patient based on both id and username and if it belongs to the same doctor that iam sign in with 
      authntic = patient_doctor.query.filter_by(patient_id =id, doctor_id =doctor_id).first()
      
      if authntic : 
        patienttt = patient.query.filter_by(id=id, username=username).first()
        
        if patienttt:
            # Patient found, retrieve the patient's details
            patient_data = {
                "id": patienttt.id,
                "username": patienttt.username,
                "email": patienttt.email,
                "First_name": patienttt.First_name,
                "Last_name": patienttt.Last_name,
                "Age": patienttt.Age,
                "data_of_birth": patienttt.data_of_birth,
                "disease": patienttt.disease,
            }
    
            # Pass the patient data to the template to display
            return render_template('patint_fetch.html', title='Clinic Application', form=form, patient=patient_data)
      else:
            # No matching found
            form.username.errors.append("This patient is not asigend to you or dosn't exist")
            return render_template('patint_fetch.html', title='Clinic Application', form=form, patient=None)
    form.username.errors.append("this patient dosn't exist")
    return render_template('patint_fetch.html', title='Clinic Application', form=form, patient=None)
   
# add new patient to be asigend to spacfic doctor and add it's id and the asigend doctor id to the many to many table
@app.route('/patient_signup', methods=['GET', 'POST'])
def patient_signup():
    
    doctor_id = session.get('unique_id')  
    if not doctor_id:
        return redirect('/signin')  

    form = patint_Sign_up_Form()
    if request.method == "GET":
        return render_template('patint_sign_up.html',form=form)
    
    elif request.method == "POST"and form.validate_on_submit():
        
       username =  form.username.data
       email = form.email.data
       password = form.password.data
       First_name = form.First_name.data
       Last_name = form.Last_name.data
       Age = form.Age.data
       data_of_birth = form.data_of_birth.data
       disease = form.disease.data
       id = form.id.data
       
       new_mix = patient_doctor( doctor_id = doctor_id , patient_id = id)
       new_patient = patient(username=username,email=email,password=password,First_name=First_name,Last_name=Last_name,Age=Age,data_of_birth=data_of_birth,disease=disease, id=id)
       db.session.add(new_patient)
       db.session.add(new_mix)
       db.session.commit()
       return redirect('/swip')
     # No matching found
    form.confirm_password.errors.append('')
    return render_template('patint_sign_up.html', form=form) 
    
# doctor signup to recored new doctor and append it to the database 
@app.route('/signup', methods=['GET', 'POST'])
def doctor_signup():
    form = Doctor_sign_up_Form()
    if request.method == "GET":
        return render_template('doctor_sign_up.html',form=form)
    
    elif request.method == "POST"and form.validate_on_submit():
        
       unique_id = form.unique_id.data
       doctor_name = form.doctor_name.data
       password = form.password.data
       doctor_speciality = form.doctor_speciality.data
       
       new_doctor = doctor(unique_id=unique_id, doctor_name=doctor_name, password=password, doctor_speciality=doctor_speciality)
       db.session.add(new_doctor)
       db.session.commit()
        
       return redirect('/signin')
     # No matching found
    form.confirm_password.errors.append('')
    return render_template('doctor_sign_up.html', form=form) 

# doctor signin form
@app.route('/signin', methods=['GET', 'POST'])
def doctor_signin():
    form = Doctor_sign_in_Form()
    if request.method == 'GET':
        return render_template('doctor_sign_in.html',title ='Clinic Application', form=form)
    
    elif request.method == 'POST'and form.validate_on_submit():
        
        unique_id = form.unique_id.data
        password = form.password.data
        doctorr = doctor.query.filter_by(unique_id=unique_id, password =password).first()
        
        if doctorr:
            session['unique_id'] = doctorr.unique_id
            return redirect('/swip')
        
        else:
            # No matching doctor found
            form.password.errors.append("invalied username or password")
            return render_template('doctor_sign_in.html', title='Clinic Application', form=form)



# future futers :

# --- add new for same patient ---- 
# @app.route('/patient_new_record', methods=['GET', 'POST'])
# def patient_new(): 

# --- delet patient ---- 
#@app.route('/patient_delet', methods=['GET', 'POST'])
# def patient_delet():
# --- print patint info in pdf form ---- 
#@app.route('/patient_pdf', methods=['GET', 'POST'])
# def download_pdf():

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True , port=8080)


    
