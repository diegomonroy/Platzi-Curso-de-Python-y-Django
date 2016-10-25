from flask import Flask, url_for, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

# @app.route("/form/", methods['GET', 'POST'])
# def form():
# 	if request.method == 'POST':
# 		return "Esto es un POST!"
# 	else :
# 		return "Hello World!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
	url_for('static', filename='style.css')
	return render_template("hello.html", name = name)

@app.route("/url2")
def url_nueva():
	return "Yo soy otra URL"

@app.route("/post/<int:post_id>")
def mostrar_post(post_id):
	return "Post %d" % post_id

@app.route("/usuario/<username>")
@app.route("/user/<username>")
def show_user_profile(username):
	return "User %s" % username

if __name__ == "__main__":
	app.debug = True
	# app.run()
	app.run(host='0.0.0.0', port=3000)