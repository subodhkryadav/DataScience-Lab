from flask import Flask,render_template,request

app=Flask(__name__)
@app.route("/")
def home():
    return "This is the Home page"

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form["name"]
        return f"THIS is {name}"
    return render_template("submit.html")

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        name=request.form["name"]
        return f"THIS is {name}"
    return render_template("submit.html")

if __name__=="__main__":
    app.run(debug=True)