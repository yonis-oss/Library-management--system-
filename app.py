from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Library Management System</h1>
    <p>Welcome to our Library!</p>
    """

if __name__ == "__main__":
    app.run()
