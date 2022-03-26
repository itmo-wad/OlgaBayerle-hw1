from flask import Flask, render_template,redirect, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)


@app.route("/") 
def default():
    return redirect(url_for('profile'))
    
@app.route("/profile")
def profile():
    return render_template("cv.html")

@app.route('/profilepicture')
def profilepicture():
    return app.send_static_file('profilepicture.jpeg')


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)