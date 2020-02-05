from flask import Flask, render_template
from twilio.rest import Client
app = Flask(__name__)

client = Client('id', 'token')

@app.route('/one')
def page_one():
	return render_template("one.html")

@app.route('/two')
def page_two():
	return render_template("two.html")

@app.route('/text_one', methods=["POST"])
def text_one():
	message = client.messages.create(to="+16093690255", from_="+12013409962", body="You liked a dog!")
	return "Hey, I like dogs!"

@app.route('/text_two', methods=["POST"])
def text_two():
	message = client.messages.create(to="+16093690255", from_="+12013409962", body="You liked a cat!")
	return "Hey, I like cats!"
