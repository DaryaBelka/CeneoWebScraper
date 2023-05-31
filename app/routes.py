from flask import Flask,render_template
import requests
import json
import matplotlib
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Darya Belka!"

@app.route('/name/',defaults={'name': "Anonim"})
@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"

@app.route('/')
@app.route('/index')
def index():
    return render_template('mainpage.html')




