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

@app.route('/setup',methods=['GET','POST'])

def prediction():
    data=request.get_json(force=True)
    print(data)
    return "done"

