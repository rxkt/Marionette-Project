from flask import flask, render_template , session , redirect , request

app = Flask(__name__)

@app.route("/")
def home():
    if 'username' in session:
        return render_template("test.html")
    else:
        return render_template("test.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0" , port = 8000)
