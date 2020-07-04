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

    print(req)

    as_string = req['input']

    checked = profanity.contains_profanity(as_string)

    print(checked)

    res = make_response(jsonify(checked), 200)

    censored = profanity.censor(as_string, '*')

    print(censored)

    res2 = make_response(jsonify(censored), 200)

    # custom = []
    # profanity.add_censor_words(custom)

    return res
    # return res2
    return render_template("home.html")