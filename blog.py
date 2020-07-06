from flask import Flask,render_template,url_for,request,redirect,session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "linuxdegilgnulinux"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/burak/Desktop/ilteris_flask/blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")







if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)