from flask import Flask
"""it creates an instance of the Flask class,
    which will be your WsGI(web server gateway interface) application
"""
# this is the Wsgi applicataion
app=Flask(__name__)

# crate the first route this is also the home page just like the google home page
@app.route("/")
def welcome():
    return "This side subodh kumar yadav and this is the flask clases"

# in this type of multiple rout will be created
@app.route("/index")
def index():
    return "Hey subodh this is the index route"

# below is the entry point of the falsk web app
if __name__=="__main__": 
    app.run(debug=True)  # the debug=True means update and restart
