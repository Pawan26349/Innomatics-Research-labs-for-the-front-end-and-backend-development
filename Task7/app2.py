from flask import Flask,request,render_template

app = Flask(__name__)

##############################################

notes = []

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template('home2.html')
    else:
        note = request.form.get('note')
        if(len(note)!=0):
            notes.append(note)
        return render_template('home2.html',notes=notes)
    
@app.route('/deletion',methods=['POST'])
def deletion():
    if(len(notes)!=0):
        notes.pop()
    return render_template('home2.html',notes=notes)

##############################################

if __name__ == '__main__':
    app.run(debug=True)