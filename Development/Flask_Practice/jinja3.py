from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def home():
    return "This is the Homa page"

@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>50:
        res= "PASSED"
    else:
        res= "FAILED"
    
    return render_template("result.html",results=res)

if __name__=="__main__":
    app.run(debug=True)