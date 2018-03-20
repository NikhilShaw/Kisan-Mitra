from flask import Flask, session, render_template, request, url_for, redirect
import sckit
import feats
import csv
import pandas as pd
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def first(): 
	return redirect(url_for('index'))

@app.route('/index.html')
def index(): 
	return render_template('index.html')



@app.route('/index.html', methods=['POST'])
def indexafter():
	username=request.form['id']
	password=request.form['Password']
	if password=='     ' and username in ['champa', 'ratan']:
		if username=='champa':
			session['curr_user']='champa'
			return render_template('profile.html')
		else:
			session['curr_user']='ratan'
			return render_template('profile2.html')
	else:
		return render_template('invalidprofile.html')

@app.route('/invalidprofile.html')
def invalidprofile():
	return render_template('invalidprofile.html')

@app.route('/invalidprofile.html', methods=['POST'])
def invalidprofileafter():
	username=request.form['id']
	password=request.form['Password']
	if password=='     ' and username in ['champa', 'ratan']:
		if username=='champa':
			session['curr_user']='champa'
			return render_template('profile.html')
		else:
			session['curr_user']='ratan'
			return render_template('profile2.html')
	else:
		return render_template('invalidprofile.html')



@app.route('/dhanmandi.html')
def dhanmandi():
	return render_template('dhanmandi.html')

@app.route('/dronereport.html')
def dronereport():
	return render_template('dronereport.html')

@app.route('/loanpage.html')
def loanpage():
	return render_template('loanpage.html')

@app.route('/loanpage.html', methods=['POST'])
def loanpageafter():
	loandata=[]
	loandata.append(request.form['Bank'])
	loandata.append(request.form['firstname'])
	loandata.append(request.form['middlename'])
	loandata.append(request.form['lastname'])
	loandata.append(request.form['houseno'])
	loandata.append(request.form['locality'])
	loandata.append(request.form['pincode'])
	loandata.append(request.form['amount'])
	loandata.append(request.form['time'])
	with open('loan_details.csv', 'a') as f:
		writer=csv.writer(f)
		writer.writerow(loandata)
	return render_template('loanpage_redirect.html')

@app.route('/prediction.html')
def prediction():
	return render_template('prediction.html')

#params=[str soil type, int whc, int rainmin, int rainmax,
#int tempmin, int tempmax, float phmin, floatphmax]

@app.route('/prediction.html', methods=['POST'])
def prediction_submit():
	input_date=request.form['date']
	dt=datetime.strptime(input_date, '%Y-%m-%d')
	ma, mi, pre=feats.get_temp_and_pre(dt.month)
	params=["clayey loamy", 2, pre, mi, ma, 6.7, 7.7]
	l=sckit.predict_crop(params)
	l=''.join(l[0])
	return render_template('redirectp.html', recc_crop=l)

@app.route('/profile.html')
def profile():
	if session['curr_user']=='champa':
		return render_template('profile.html')
	else:
		return render_template('profile2.html')

@app.route('/profile2.html')
def profile2():
	if session['curr_user']=='champa':
		return render_template('profile.html')
	else:
		return render_template('profile2.html')


@app.route('/redirectp.html')
def redirectp():
    return render_template('redirectp.html')


@app.route('/schemes.html')
def schemes():
    return render_template('schemes.html')

