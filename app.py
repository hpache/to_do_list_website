from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, TodoModel
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://thdubczkubqtdu:11b1f97cf5af521451340de904ba9ce1a6d4ae1d1b04bb6fc0026a0a779d1b77@ec2-54-160-103-135.compute-1.amazonaws.com:5432/d50g0qitf4h4pp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def index():
    completeTodos = TodoModel.query.filter_by(completed = True)
    incompleteTodos = TodoModel.query.filter_by(completed = False)
    return render_template("todo.html", incomplete=incompleteTodos, complete = completeTodos)

@app.route("/add", methods = ["POST"])
def add():
    item = request.form["todoItem"]
    currentDate = date.today()
    priority = request.form["priority"]
    tag = request.form["tag"]
    item = TodoModel(item=item, date=currentDate, priority=priority, tag=tag)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/remove", methods = ["POST"])
def update():
    db.session.query(TodoModel).filter_by(id = request.form["remove"]).delete()
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete", methods = ["POST"])
def complete():
    todo = TodoModel.query.filter_by(id = request.form["complete"]).first()
    todo.completed = True 
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)