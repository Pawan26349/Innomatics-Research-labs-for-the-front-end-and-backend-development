# firstly we import the Flask class from flask module.
from flask import Flask,request

# Here we create the object of the Flask class.
app = Flask(__name__)


# Here we write the route of the app.
################################################

@app.route('/')
def home():
    return "Welcome to my first backend server made with flask."

@app.route('/about')
def about():
    return "This is the backend that we made to take the query parameter and return the uppercase of that one."

@app.route('/user')
def username():
    username = request.args.get('username')
    password = request.args.get('password')

    # lst = ["your user name is : "+username,"\n Your password is : "+password]
    final = "your user name is : "+username.upper() +" Your password is : "+password

    return final

@app.route('/calc')
def arithmetic_operation():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    lst = ["sum : "+str(int(num1)+int(num2)),"subtraction : "+str(int(num1)-int(num2)),"multiplication : "+str(int(num1)*int(num2)),"Division : "+str(int(num1)/int(num2))]

    return lst





################################################

# Here we run the app
if __name__ == '__main__':
    app.run(debug=True)