from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

###########################################################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/regex101',methods=['GET','POST'])
def regex():
    if request.method == 'POST':
        str1 = request.form.get('regular_expression')
        str2 = request.form.get('check_text')
        # lst = work(reg,text_area)
        n = len(str1)
        data = list([str2[i:i+n] for i in range(0, len(str2))])
        new_lst = []

        for i in data :
            if str1 == i:
                new_lst.append(i)

        if len(new_lst)!=0:
            return render_template('result.html',result=new_lst)
        else:
            return render_template('result.html',result=["the string is not matched"])
        
    else:
        return render_template('regex.html')




###########################################################


if __name__ == '__main__':
    app.run(debug=True)