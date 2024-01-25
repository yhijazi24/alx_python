"""
This script demonstrates a Flask web application with five routes.
"""

# Import necessary module
from flask import Flask, abort

"""
Create a Flask application instance.
"""
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root path.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the /hbnb path.

    Returns:
        str: Message "HBNB".
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route handler for the /c/<text> path.

    Args:
        text (str): The value of the text variable.

    Returns:
        str: Message "C " followed by the value of the text variable.
    """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is cool'):
    """
    Route handler for the /python/<text> and /python paths.

    Args:
        text (str): The value of the text variable (default is 'is cool').

    Returns:
        str: Message "Python " followed by the value of the text variable.
    """
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route handler for the /number/<n> path.

    Args:
        n (int): The value of the n variable.

    Returns:
        str: Message "<n> is a number" if n is an integer, otherwise 404 error.
    """
    return '{} is a number'.format(n)

if __name__ == '__main__':
    """
    Main block to run the Flask application.

    Starts the development server on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
