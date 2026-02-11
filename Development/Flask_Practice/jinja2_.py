from flask import Flask, render_template,request
app=Flask(__name__)

#varibale rule

#addition
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    sum=a+b
    return f"sum of the given number is: {sum}"

#multiplication
@app.route("/multiplication/<int:a>/<int:b>")
def multi(a,b):
    m=a*b
    return f"multiply of the given number is: {m}"


if __name__=="__main__":
    app.run(debug=True)