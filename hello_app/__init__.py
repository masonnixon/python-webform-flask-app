from flask import Flask  # Import the Flask class
from flask_bootstrap import Bootstrap
app = Flask(__name__)    # Create an instance of the class for our use

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'Du4wHBTUKeelbceT5w3nBh6tXlH68VFE'

# Flask-Bootstrap requires this line
Bootstrap(app)