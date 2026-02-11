from flask import Flask

app=Flask(__name__)

@app.route("/")
def sum():
    a=int(input("Enter the first Number: "))
    b=int(input("Enter the second Number: "))
    sum=a+b
    print(f'this is not working properly so the sum is: {sum}')
# entry of the falsk app
if __name__=="__main__":
    app.run(debug=True)

