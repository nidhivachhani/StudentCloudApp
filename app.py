from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Student Information Web Application!</h1>
    <p>Application is successfully deployed on the cloud.</p>
    """

@app.route("/database")
def database():
    try:
        connection = psycopg2.connect(os.environ.get("DATABASE_URL"))
        connection.close()
        return "<h2>Cloud Database Connected Successfully!</h2>"
    except Exception as e:
        return "<h2>Database Connection Error</h2><p>" + str(e) + "</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)