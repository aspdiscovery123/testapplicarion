# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:59:18 2023

@author: DELL
"""

from flask import Flask,request

app=Flask(__name__)

@app.route('/home')

def application():
    return "hello from ashish"

@app.route('/testing',methods=['GET','POST'])

def prediction():
    json_body = request.get_json()
    #print(data)
    return "done"

