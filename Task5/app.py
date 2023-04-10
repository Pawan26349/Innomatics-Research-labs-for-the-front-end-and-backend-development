from flask import Flask ,request,render_template

app = Flask(__name__)

#################################################

# Routing area.

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/add',methods=['POST'])
# def addition():
#     num1 = request.args.get('var_1')
#     num2 = request.args.get('var_2')
#     return (str(int(num1)+int(num2)))


# this is the first one that is used for the get request.

@app.route('/add')
def add2():
    num1 = request.args.get('var_1')
    num2 = request.args.get('var_2')
    return (str(int(num1)+int(num2)))

# this is the second one that handles both the request.

@app.route('/addition',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        num1 = request.form.get('var_1')
        num2 = request.form.get('var_2')
        return (str(int(num1)+int(num2)))
    else:
        return render_template('addition.html')
    


#################################################

if __name__ == '__main__':
    app.run(debug=True)