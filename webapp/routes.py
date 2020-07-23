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

    req = request.get_json()

    # print(req)

    as_string = req['input']

    checked = "Yes" if profanity.contains_profanity(as_string) == True else "No"
    
    # print(checked)

    censored = profanity.censor(as_string, '🙉')

    count = censored.count('🙉')

    # print(censored)

    res = make_response(jsonify(f'Contains profanity? {checked}. Profanity count: {count}. Here: "{censored}"'), 200)

    # custom = []
    # profanity.add_censor_words(custom)

    return res 
    return render_template("home.html")