from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("get_result.html")

@app.route("/success/<int:score>")
def success(score):
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"

    exp = {
        "score": score,
        "res": res
    }

    return render_template("result.html", result=exp)

@app.route("/submit", methods=["POST"])
def submit():
    science = float(request.form["science"])
    math = float(request.form["math"])
    c = float(request.form["c"])
    data_science = float(request.form["datascience"])

    total_score = (science + math + c + data_science) / 4
    return redirect(url_for("success", score=int(total_score)))

if __name__ == "__main__":
    app.run(debug=True)
