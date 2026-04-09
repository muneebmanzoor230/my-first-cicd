from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Muneeb 🚀 Your CI/CD is LIVE!"
    return "🚀 Muneeb's CI/CD Project is LIVE"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
