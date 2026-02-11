## use to the jinj2 templete 
    ## used the template engine
# 1. {{}}- expression to print the output
# 2. {%   %} - use to the condition or looping
# 3. {#..#}--- use to this comment
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def home():
    return "this is the home page"

@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>50:
        res="PASSED"
    else:
        res="FAILED"
    exp={"score":score,"res":res}
    return render_template("result1.html",results=exp)

if __name__=="__main__":
    app.run(debug=True)