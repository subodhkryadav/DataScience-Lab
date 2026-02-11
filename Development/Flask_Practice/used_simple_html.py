from flask import Flask
app=Flask(__name__)
# create the first route use in the html tag
@app.route("/")
def information():
    return "<html><H1>Hi I am subodh Kumar Yadav</H1></html>"

if __name__=="__main__":
    app.run(debug=True)
