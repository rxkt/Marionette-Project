import db
from flask import Flask, render_template , session , redirect , request
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'B&S'
app.config['DEBUG']=True 

def authenticate(func):
    @wraps(func)
    def inner():
        if 'username'in session:
            return func()
else:
    return redirect('/login')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method== 'GET':
        return render_template('login.html')
    button = request.form['button']
    username = request.form['username']
    password = request.form['password']
    
    if button == 'cancel':
        return redirect('/login')
else:
    criteria = {'username': username, 'password': password}
    user = db.find_user(criteria)
    if user:
        session['username'] = username

        return redirect('/')
else:
    return render_template('test.html')

@app.route('/register', methods=['GET', 'POST'])

def register():
    if request.method == 'GET':
        return render_template('register.html')
    button = request.form['button']
    username = request.form['username']
    password = request.form['password']
    first = request.form['first']
    last = request.form['last']
    if button == 'cancel':
        return redirect('/register')
    else:
        if not password or not first or not last:
            return render_template('register.html',error='incomplete')
        criteria = {'username': username}
        if db.find_user(criteria):
            return render_template('register.html',error='username taken')
        else:
            
            user_params = {'username': username, 'password': password, 'first': first, 'last': last}
            db.new_user(user_params)
            
            return render_template('login.html',error="Created")


if __name__ == "__main__":
    app.secret_key='B&S'
    app.debug = True
    app.run()
    
    
