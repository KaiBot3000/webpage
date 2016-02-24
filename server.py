from flask import Flask, render_template
from flask_restful import Api
from magic import Magic, Language, replies
# import random


app=Flask(__name__)
api = Api(app)

# not an actual secret, as I'm not using encrypted sessions
app.secret_key = 'forage_the_things'


@app.route('/')
def index():			                                              
	
	return render_template('home.html')


@app.route('/clump')
def clump():                                                          
    
    return render_template('clump.html')


api.add_resource(Magic, "/magic8pi/v1/", "/magic8pi/v1/<string:language>")
api.add_resource(Language, "/magic8pi/v1/languages")


if __name__ == "__main__":
	app.run(debug=True)
	
