
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    text1 = request.form.get("text1")
    text2 = request.form.get("text2")
    return render_template("result.html", result={"text1": text1, "text2": text2})

if __name__ == "__main__":
    app.run(debug=True)
