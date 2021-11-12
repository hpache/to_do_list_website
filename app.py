from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')

@app.route("/")

def index():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)