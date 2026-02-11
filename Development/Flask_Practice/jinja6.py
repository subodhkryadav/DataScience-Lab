# use to the jinja template engine
from flask import Flask,render_template,request
app=Flask(__name__)

## home page route
@app.route("/")
def home():
    return "This is the first page"

@app.route("/successif/<int:number>")
def successif(number):

    return render_template("result2.html",results=number)
    

if __name__=="__main__":
    app.run(debug=True)

