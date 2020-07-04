from webapp import app
from flask import render_template, redirect, url_for, request, jsonify, make_response
from better_profanity import profanity

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/result', methods=["POST"])
def result():
    return render_template("result.html")