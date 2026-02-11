## 1. Building URL dynamicaaly
## 2. Variable Ruele
## 3. Jinja 2 Template Engine

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def home():
    return "This is the Home page"

@app.route('/submit',methods=["GET","POST"])
def submit():
    if request.method=="POST":
        name=request.form["name"]
        return f"This is {name}"
    return render_template("submit.html")


# now create a route
@app.route("/success/<score>")                  #
def score(score):                               #  This is the var rule here all are present in the form of integer
    return f"you marks is: {score}"             #


if __name__=="__main__":
    app.run(debug=True)
