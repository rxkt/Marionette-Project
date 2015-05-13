import db
from flask import Flask, render_template , session , redirect , request
from flask.ext.socketio import SocketIO, emit
"""

from firebase import firebase
firebase = firebase.FirebaseApplication('https://boiling-heat-3848.firebaseio.com',None)

"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'B&S'
socketio = SocketIO(app)

@app.route("/")
def mainpage():
    
    if 'username' in session:
        inses= True
        print session['username']
    else:
        inses= False
        print "not in session"
    print inses
    return render_template("test.html",inses=inses)

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
   
    mainpage()
    


        
        
        

if __name__ == "__main__":
    app.secret_key='B&S'
    app.debug = True
    
    socketio.run(app)
    app.run()
    
    
