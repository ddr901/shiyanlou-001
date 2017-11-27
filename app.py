#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,abort
import json
import os


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

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
    
if __name__ == '__main__':
    app.run()
