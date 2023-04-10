from flask import Flask,request

app = Flask(__name__)

##############################################

@app.route('/')
def home():
    return "Hello to all the people you are on the Home Page."

@app.route('/add')
def addition():
    a = request.args.get('num1')
    b = request.args.get('num2')

    return(str(int(a)+int(b)))

@app.route('/search')
def search():
    return "You are on the search end point."

@app.route('/search',methods=['POST'])
def search2():
    return "you are on the post method of the search end point.\n"


# Now we do some dynamic routing .

user_names = ["pawan","prateek","peeush","naman"]

@app.route('/in/<user>')
def search3(user):
    if(user in user_names):
        return "Hello sir welcome to your profile."
    else:
        return "Sorry sir you have to first register with us ."
##############################################

if __name__ == '__main__':
    app.run(debug=True)