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
@socketio.on('login')
def home(email=None, password=None):
    if 'username' in session:
        print('test: ' + str(email) + "  " + str(password))
        return render_template("test.html")
    else:
        print('test: ' + str(email) + "  " + str(password))
        return render_template("test.html")

if __name__ == "__main__":
    app.debug = True
    socketio.run(app)
    
