from flask import Flask, render_template

app=Flask(__name__)

# not an actual secret, as I'm not using sessions
app.secret_key = 'forage_the_things'


@app.route('/')
def index():			                                              
	
	return render_template('home.html')


@app.route('/clump')
def clump():                                                          
    
    return render_template('clump.html')


if __name__ == "__main__":
	app.run(debug=True)
	
