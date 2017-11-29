#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,ForeignKey
from datetime import datetime
import json
import os


app = Flask(__name__)
app.config.update(dict(SQLALCHEMY_DATABASE_URI= 'mysql://root@localhost/shiyanlou'))
db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File') 
    def __init__(self,name):
        self.name = name

class File(db.Model):
    __tablename__ = 'File'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),unique=True)
    created_time = db.Column(db.DateTime)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    category = db.relationship('Category')
    def __init__(self,title,content,category,created_time=None):
        self.title = title
        self.content = content
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time
        self.category = category
        
    def add_tag(self, tag_name):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            mongo.files.update_one({'file_id': self.id}, {'$set': {'tags': tags}})
        else:
            tags = [tag_name]
            mongo.files.insert_one({'file_id': self.id, 'tags': tags})
        return tags

    def remove_tag(self, tag_name):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            try:
                new_tags = tags.remove(tag_name)
            except ValueError:
                return tags
            mongo.files.update_one({'file_id': self.id}, {'$set', {'tags': new_tags}})
            return new_tags
        return []

    @property
    def tags(self):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            print(file_item)
            return file_item['tags']
        else:
            return []    
        

def insert_datas():
    java = Category('Java')
    python = Category('python')
    file1 = File('Hello Java',datetime.utcnow(),java, 'File Content -Java is cool!')
    file2 = File('Hello Python',datetime.utcnow(),python, 'File Content -Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')

@app.route('/')
def index():
    return render_template('index.html',files=File.query.all())
           

@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id) 
    return render_template('file.html',file_item=file_item)
@app.errorhandler(404)
def Not_Found(error):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run()
