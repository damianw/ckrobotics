import os
from flask import Flask,render_template,send_from_directory
import pyjade
from flask.ext.login import LoginManager

app = Flask(__name__)
# use the jade template engine
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def index():
	obj = {
		"title": "Cranbrook Kingswood Robotics",
		"short_title": "CK Robotics",
		"header_text": "Coming soon!",
		"header_info": "Welcome to the website for the Cranbrook Kingswood Robotics teams! The website is currently under construction, but come back soon for team blogs, robot details, and more!",
		"pretty": "true"
	};
	return render_template('index.jade', **obj)

# this guy handles static files
@app.route('/<path:filename>')
def send_pic(filename):
	print(filename)
	return send_from_directory('./public/', filename)

if __name__ == '__main__':
	# Bind to PORT if defined (environment variable on heroku)
	port = int(os.environ.get('PORT', 3000))
	
	app.run(host='0.0.0.0', port=port, debug=True)


