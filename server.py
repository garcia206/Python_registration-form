from flask import Flask, render_template, request, redirect, session, flash
import random
import re


app = Flask(__name__)
app.secret_key = 'ThisIsSecretsszs'

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():

    if len(request.form['email']) < 1:
        flash('Email cannot be blank!', 'Error')
        return redirect('/')
    elif len(request.form['fname']) < 1:
        flash('First Name cannot be blank!', 'Error')
        return redirect('/')
    elif len(request.form['lname']) < 1:
        flash('Last Name cannot be blank!', 'Error')
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash('Password must be at least 8 characters!')
        return redirect('/')
    elif len(request.form['cpassword']) < 1:
        flash('Please confirm your password!')
        return redirect('/')
    elif re.search(r"[0-9]", request.form['fname']) or re.search(r"[0-9]", request.form['lname']):
        flash('No numbers allowed in your Name!')
        return redirect('/')
    elif request.form['password'] != request.form['cpassword']:
        flash('Your passwords don\'t match!')
        return redirect('/')
    else:
        flash("Your information was successfully submitted. Thank you!")

    return redirect('/')

app.run(debug=True) # run our server
