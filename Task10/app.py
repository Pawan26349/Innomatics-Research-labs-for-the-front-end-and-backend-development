from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app=Flask(__name__)

#SQL Alchemy Configuration
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
Migrate(app,db)

#Create a Model

class Sabji(db.Model):
    __tablename__='sabjis'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text)
    mrp=db.Column(db.Integer)

    def __init__(self, name, mrp):
        self.name=name
        self.mrp=mrp

    def __repr__(self):
        return "Sabji Name {} and MRP {}".format(self.name, self.mrp)
    



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add',methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form.get('in_1')
        mrp = int(request.form.get('in_2'))
        new_sabji = Sabji(name, mrp)
        db.session.add(new_sabji)
        db.session.commit()
    return render_template('add.html')

@app.route('/display')
def display():
    sabjis = Sabji.query.all()
    return render_template('display.html',sabji = sabjis)

@app.route('/search')
def search():
    return render_template('search.html')

if __name__=='__main__':
    app.run(debug=True)


# from flask import Flask,request,render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import os

# app = Flask(__name__)

# # ##############SQL configution#################

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(basedir,'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# Migrate(app, db)

# # ##############################################

# # ################ Sql Model(table) making #####################

# class Sabji(db.Model):
#     __tablename__ = "sabjis"
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.Text)
#     mrp = db.Column(db.Integer)

#     def __init__(self, name, mrp):
#         self.name = name
#         self.mrp = mrp
    
#     def __repr__(self):
#         return "Sabji Name - {} and mrp is {} ".format(self.name, self.mrp)


# # ##############################################################


# ###########route and function binding#########

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/add',methods=["GET","POST"])
# def add():
#     if request.method == "POST":
#         name = request.form.get('in_1')
#         mrp = int(request.form.get('in_2'))
#         new_sabji = Sabji(name, mrp)
#         db.session.add(new_sabji)
#         db.session.commit()
#     return render_template('add.html')



# @app.route('/display')
# def display():
#     sabjis = Sabji.query.all()
#     return render_template('display.html',sabji = sabjis)

# @app.route('/search')
# def search():
#     return render_template('search.html')

# # @app.before_first_request
# # def create_tables():
# #     db.create_all()
# ##############################################


# if __name__ == '__main__':
#     app.run(debug=True)