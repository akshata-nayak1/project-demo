import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

model = pickle.load(open('creditp.pkl', 'rb'))
import imutils
import sklearn
from flask import Flask, render_template, request, redirect, url_for,session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import re
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
from sklearn.metrics import confusion_matrix
warnings.filterwarnings('ignore')


from sqlalchemy import func
from sqlalchemy import or_


# Configuring Flask
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

@app.before_request
def create_tables():
    db.create_all()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/form')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    error=''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['logged_in'] = True
        session['username'] = username
        global user
        user = User.query.filter_by(username=username).first()
        if not user or user.password != password:
            error = 'Invalid username or password.'
            return render_template('login.html', error=error)
        #return redirect(url_for('upload'))
        return render_template('index.html')
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    c=0
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'cpassword' in request.form:
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['cpassword']
        account = User.query.filter_by(username=username).first()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must not contain any special characters!'
        elif not username or not password or not confirm_password:
            msg = 'Please fill out the form !'
        elif password != confirm_password:
            msg = 'Passwords do not match.'
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            c=1
            msg = 'You have successfully registered!'
            #return render_template('signup.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return redirect(url_for('signup'))
    if c==1:
        return render_template('login.html')
    return render_template('signup.html',error=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return render_template("service.html")


@app.route('/process')
def process_file():
    
        # Render the template with the entire DataFrame
    return redirect('https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud')


@app.route('/predict',methods=['POST'])
def predict():

    time=request.form['time']
    time=float(time)

    v1=request.form['v1']
    v1=float(v1)

    v2=request.form['v2']
    v2=float(v2)

    v3=request.form['v3']
    v3=float(v3)

    v4=request.form['v4']
    v4=float(v4)

    v5=request.form['v5']
    v5=float(v5)
    
    v6=request.form['v6']
    v6=float(v6)

    v7=request.form['v7']
    v7=float(v7)

    v8=request.form['v8']
    v8=float(v8)

    v9=request.form['v9']
    v9=float(v9)

    v10=request.form['v10']
    v10=float(v10)
    
    v11=request.form['v11']
    v11=float(v11)

    v12=request.form['v12']
    v12=float(v12)

    v13=request.form['v13']
    v13=float(v13)

    v14=request.form['v14']
    v14=float(v14)

    v15=request.form['v15']
    v15=float(v15)
    
    v16=request.form['v16']
    v16=float(v16)

    v17=request.form['v17']
    v17=float(v17)

    v18=request.form['v18']
    v18=float(v18)

    v19=request.form['v19']
    v19=float(v19)

    v20=request.form['v20']
    v20=float(v20)

    v21=request.form['v21']
    v21=float(v21)

    v22=request.form['v22']
    v22=float(v22)
    
    v23=request.form['v23']
    v23=float(v23)

    v24=request.form['v24']
    v24=float(v24)

    v25=request.form['v25']
    v25=float(v25)
    
    v26=request.form['v26']
    v26=float(v26)

    v27=request.form['v27']
    v27=float(v27)

    v28=request.form['v28']
    v28=float(v28)
    
   

    amount=request.form['amount']
    amount=float(amount)


    
    
    
    
   
    int_features = [time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,
    v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,
    v25,v26,v27,v28,amount]

    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    

    return render_template('result.html', prediction_text='The Passenger {}'.format(prediction[0]),prediction=prediction)



if __name__ == "__main__":
    app.run(debug=True)
    
    
