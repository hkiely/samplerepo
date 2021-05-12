from flask import render_template

from app import app

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/brands')
def brands():
	return render_template("brands.html")


@app.route('/account')
def account():
	return render_template("account.html")