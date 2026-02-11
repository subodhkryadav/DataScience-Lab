from flask import Flask

app=Flask(__name__)
# now we create the flask route
@app.route("/")
def first_route():
    return "This is the main or first or Home page of the flask app"

@app.route("/second")
def second():
    return "This is the second route of the flask app"

@app.route("/third")
def third():
    return "this is the third route of the entire flask app" 

if __name__=="__main__":
    app.run(debug=True)