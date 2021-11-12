from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, InfoModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://thdubczkubqtdu:11b1f97cf5af521451340de904ba9ce1a6d4ae1d1b04bb6fc0026a0a779d1b77@ec2-54-160-103-135.compute-1.amazonaws.com:5432/d50g0qitf4h4pp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

@app.route("/")
def index():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)