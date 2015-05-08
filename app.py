from flask import Flask, render_template , session , redirect , request
from flask.ext.socketio import SocketIO, emit
"""

from firebase import firebase
firebase = firebase.FirebaseApplication('https://boiling-heat-3848.firebaseio.com',None)

"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello'
socketio = SocketIO(app)

@app.route("/")
def homez():
    return render_template("test.html")

@socketio.on('login')
def home(emailpassword={'email':None,'password':None}):
    print('it works1')
    if 'username' in session:
        print("chris is a bum")
       ## print('test: ' + str(email) + "  " + str(password))
        
    else:
        
        print('test: ' + str(emailpassword['email']) + "  " + str(emailpassword['password']))
        
        

if __name__ == "__main__":
    app.debug = True
    socketio.run(app)
    
