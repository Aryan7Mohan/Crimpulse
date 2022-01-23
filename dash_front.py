from flask import Flask, render_template, redirect, url_for,request
import json
import pandas as pd
import numpy as nppip
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy import create_engine
import mysql.connector
from mysql import connector
from psycopg2 import sql
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from datetime import datetime # Current date time in local system print(datetime.now())
from datetime import date
from datetime import time
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/mealplan'

db = SQLAlchemy(app)


from flask import Flask, render_template, redirect, url_for,request, flash
import os
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, DateField, ValidationError
from wtforms.validators import InputRequired, Email, Length, DataRequired, EqualTo
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import jsonify
from flask_mail import Mail, Message
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crimpulse'
# app.config['TESTING'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)




class lists(db.Model):

    id = db.Column(db.Integer(),primary_key=True)
    heading = db.Column(db.String(200))
    content = db.Column(db.String(200),nullable=True)









def add_book(the_book_name,the_price,the_image,the_details,the_author):
    info=books()
    info.book_name=the_book_name
    info.price=the_price
    info.image=the_image
    info.details=the_details
    info.author=the_author
    info.seller_id = current_user.id

    getdate = date.today()
    info.date_upload=datetime.now()
 
 
    db.session.add(info)
    db.session.commit()
    




#~~~~~~~~~~~        OPENS MAIN PAGE               ~~~~~~~~~~~~~~~~~~~~~~
@app.route('/index', methods=["GET", "POST"])
def index():


    ls=[]
    ls=show_lists()
    print(ls)

    return render_template('index.html', ls=ls)


@app.route('/index/<string:heading>', methods=["GET", "POST"])
def list_item(heading):
    ls=[]
    '''
    if request.method=="POST":
        heading=request.form["heading"]
        print(heading)
    '''

    ls=show_details(heading)


        
        

    return render_template('list_item.html', ls=ls)




@app.route('/delete_item', methods=["GET", "POST"])
def delete_item():
    ls=[]
    ls=show_lists()
    print(ls)
    if request.method=="POST":
        heading=request.form["heading"]
        cnx = mysql.connector.connect(user='root', database='crimpulse')
        cursor = cnx.cursor()

        

        
        query = """DELETE FROM lists WHERE (heading = '"""+str(heading)+"""' )  ; """

        cursor.execute(query)
        
        
        cnx.commit() 
        cursor.close()
        cnx.close()

        return redirect(url_for('index'))


        

    return redirect(url_for('index'))





@app.route('/edit_item', methods=["GET", "POST"])
def edit_item():
    if request.method=="GET":
        heading=request.form["heading"]
        cnx = mysql.connector.connect(user='root', database='crimpulse')
        cursor = cnx.cursor()

        

        
        query = """DELETE FROM lists WHERE (heading = '"""+str(heading)+"""' )  ; """

        cursor.execute(query)
        
        
        cnx.commit() 
        cursor.close()
        cnx.close()

        return redirect(url_for('index'))


        

    return redirect(url_for('index'))



@app.route('/add_form', methods=["GET", "POST"])
def add_form():
    if request.method=="POST":

        

        return render_template('add_form.html')

    

@app.route('/add_item', methods=["GET", "POST"])
def add_item():
    if request.method=="POST":
        heading=request.form["heading"]
        content=request.form["content"]

        info=lists()
        info.heading=heading
        info.content=content
        

     
     
        db.session.add(info)
        db.session.commit()

        return redirect(url_for('index'))

    

def show_details(heading):
    cnx = mysql.connector.connect(user='root', database='crimpulse')
    cursor = cnx.cursor()

    
    query = """ SELECT * FROM lists WHERE heading= '""" +str(heading)+ """' """


    cursor.execute(query)
    result=cursor.fetchall()

    #print("henlo",result)


    cursor.close()
    cnx.close()

    return result



def show_lists():
    cnx = mysql.connector.connect(user='root', database='crimpulse')
    cursor = cnx.cursor()

    
    query = """ SELECT * FROM lists """


    cursor.execute(query)
    result=cursor.fetchall()

    print("henlo",result)



    #print("hellooo   ",re)
    #print("helloooooo2:     ",re2)
    #print("price:     ",re3)
    cursor.close()
    cnx.close()

    return result





if __name__ == "__main__":
    app.run(debug=True)
     

