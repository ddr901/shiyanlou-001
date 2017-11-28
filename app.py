#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String
from datetime import datetime
import json
import os


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category %r>'% self.name

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer,db.ForeignKey('Category.id'))
   # category = db.relationship('Category',
            #backref = db.backref('files', lazy='dynamic'))
    def __init__(self,title,content,category_id,created_time=None):
        self.title = title
        self.content = content
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time
        self.category_id = category_id
    def __repr__(self):
        return '<File %r>'% self.title



@app.route('/')
def index():
    with open('/home/shiyanlou/files/helloworld.json','r') as f:
        new_helloworld = json.loads(f.read())
    with open('/home/shiyanlou/files/helloshiyanlou.json','r') as f:
        new_helloshiyanlou = json.loads(f.read())
    title = [new_helloworld['title'],
        new_helloshiyanlou['title']]
    
    return render_template('index.html',title=title)
           

@app.route('/files/<filename>')
def file(filename):
    if filename == 'helloshiyanlou':
        with open('/home/shiyanlou/files/helloshiyanlou.json','r') as f:
            r1 = json.loads(f.read())
        r1a = [r1['title'],r1['content'],r1['created_time']]  
        return render_template('file.html',r1a=r1a)

    elif filename == 'helloworld':
        with open('/home/shiyanlou/files/helloworld.json','r') as f:
            r2 = json.loads(f.read())
        r2a = [r2['title'],r2['content'],r2['created_time']]  
        return render_template('file.html',r2a=r2a)
            
    elif not filename == 'helloworld':
        return render_template('404.html'),404
    elif not filename == 'helloshiyanlou':
        return render_template('404.html'),404
@app.errorhandler(404)
def Not_Found(error):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run()
