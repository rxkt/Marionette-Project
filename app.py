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
    if request.method== 'POST':
        
        
        button = request.form['button']
        username = request.form['username']
        password = request.form['password']
        
        if button == 'Submit':
            criteria = {'username': username, 'password': password}
            user = db.find_user(criteria)
            if user!=None and username!= "":
                session['username'] = username
                print session['username']
            
                return render_template('login.html',user=session['username'])
            
            else:
                return render_template('login.html',error="wrong info")
        else:
            return redirect('/register')
    else:
        if 'username' in session:
            return render_template('login.html',error='Insession')
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
    if button == 'Cancel':
        return redirect('/login')
    else:
        if not password or not first or not last:
            return render_template('register.html',error='incomplete')
        criteria = {'username': username}
        if db.find_user({'username':username}):
            return render_template('register.html',error='username taken')
        else:
            
            user_params = {'username': username, 'password': password, 'first': first, 'last': last}
            db.new_user(user_params)
            
            return render_template('login.html',error="created")

@authenticate 
@app.route("/home")
def home():
  return render_template('home.html')
@authenticate 
@app.route("/upload",methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        
        return render_template('upload.html')
    button = request.form['button']
    name= request.form['name']
    category= request.form['category']
    desc= request.form['desc']
    quan= request.form['quantity']
    cond= request.form['cond']
    price=request.form['price']
    if not price or not desc or not quan:
        return render_template('upload.html',error=True)
    else:
        item_params={'name':name,'category':category,'desc':desc,'quantity':quan,'cond':cond,'price':price}
        db.new_item(item_params)
        print('Added new item')
        return redirect('/upload')
    
if __name__ == "__main__":
    app.secret_key='B&S'
    app.debug = True
    app.run()
    
    
