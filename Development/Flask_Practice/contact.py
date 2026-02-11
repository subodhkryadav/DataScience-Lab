from flask import Flask ,render_template 

app=Flask(__name__)

#Now create the route
@app.route("/")
def main():
    return "This is the Home page"
@app.route("/info")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)