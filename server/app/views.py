from app import app
from flask import render_template, request, jsonify
import shutil
from chatbot import simplechat

@app.route("/",methods=["GET","POST"])
def index():
    return request.values.to_dict()
        
    
#this will be the interface we use to track a whole bunch of statistics
#we'll do visualizations around these statistics as well as dynamic text for analsyis and inspection
@app.route("/dashboard",methods=["GET","POST"])
def dashboard():
    pass

#This will show us the current state of the system and how it's interacting with users
#This will be more of a print out than any actual analysis and just show us things, interaction by interaction with time stamps
@app.route("/log",methods=["GET","POST"])
def log():
    pass
