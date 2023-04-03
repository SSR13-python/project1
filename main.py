from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ""

@app.route("/upload", methods=["POST"])
def upload():
    return ""
    
if __name__ == '__main__':
    app.run(debug=True)