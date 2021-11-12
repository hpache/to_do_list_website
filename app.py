from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.environ['postgres://thdubczkubqtdu:11b1f97cf5af521451340de904ba9ce1a6d4ae1d1b04bb6fc0026a0a779d1b77@ec2-54-160-103-135.compute-1.amazonaws.com:5432/d50g0qitf4h4pp']
conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')

@app.route("/")

def index():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)