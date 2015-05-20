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
    
    if button == 'cancel' or not(valid_user):
        return redirect('/')
    else:
        criteria = {'username': username, 'password': password}
        user = db.find_user(criteria)
    if user:
        session['username'] = username

        return redirect('/')
    else:
        return render_template('login.html')

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
        return redirect('/')
    else:
        if not password or not first or not last:
            return render_template('register.html',error='incomplete')
            criteria = {'username': username}
        if db.find_user(criteria):
            return render_template('register.html',error='username taken')
        else:
            
            user_params = {'username': username, 'password': password, 'first': first, 'last': last}
            db.new_user(user_params)
            session['username'] = username
    return redirect('/')
           




@app.route("/test")
def test():
    test2 = currentname
    return render_template("test.html", inses=currentname)

@socketio.on('signup')
def home(userpassword={'user':None,'password':None}):
    db.new_user({"username":userpassword['user'],"password":userpassword['password']})
    print("You are now signed up")
    return redirect('/')
@socketio.on('login')
def login(userpassword={'user':None,'password':None}):
    criteria={'username':str(userpassword['user']),'password':str(userpassword['password'])}
    user=db.find_user(criteria)
    session['username']=criteria['username']
    currentname = session['username']
    print (currentname)
    emit('redirect', {'url':currentname})
    

@socketio.on('additem')
def addItem(itemvalues={'name':None,'price':None,'seller':None}):
    itemvalues['seller']= session['username']
    if(itemsvalues['name']!= None):
        item= db.new_item(itemvalues)
            
    
    

        
        
        

if __name__ == "__main__":
    app.secret_key='B&S'
    app.debug = True
    
    socketio.run(app)
    app.run()
    
    
