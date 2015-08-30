from flask import Flask, render_template
from jinja2 import StrictUndefined
import json

app=Flask(__name__)

app.secret_key = 'forage_the_things'


@app.route('/')
def index():			                                              
	
	return render_template('home.html')


if __name__ == "__main__":
	app.run(debug=True)
	DebugToolbarExtension(app)
