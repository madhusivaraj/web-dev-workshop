from flask import Flask, render_template
import twilio
from twilio.rest import Client
app = Flask(__name__)

client = Client('account-sid', 'auth-token')  # found on twilio console

@app.route('/one')
def page_one():
	return render_template("one.html")

@app.route('/two')
def page_two():
	return render_template("two.html")

@app.route('/text_one', methods=["POST"])
def text_one():
	message = client.messages.create(
		body="You liked a dog",
		to="your-number",  # format - +1AAABBBCCCC
		from_="trial-number"  # found on twilio console
	)
	return "hey, i like dogs"

@app.route('/text_two', methods=["POST"])
def text_two():
	message = client.messages.create(
		body="You liked a cat",
		to="your-number",  # format - +1AAABBBCCCC
		from_="trial-number"  # found on twilio console
	)
	return "hey, i like cats"


