from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/BreastCancer')
def Breast_Cancer():
    return render_template("breast.html")

@app.route('/HeartDisease')
def Heart_Disease():
    return render_template("heart.html")

if __name__=="__main__":
    app.run(port=8080,debug=True)