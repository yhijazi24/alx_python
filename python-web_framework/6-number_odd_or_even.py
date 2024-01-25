"""
This script demonstrates a Flask web application with seven routes.
"""

# Import necessary module
from flask import Flask, render_template, abort

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
        str: Message "<n> is a number" if n is an integer.
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Route handler for the /number_template/<n> path.

    Args:
        n (int): The value of the n variable.

    Returns:
        str: HTML page with H1 tag: "Number: n" if n is an integer.
    """
    if isinstance(n, int):
        return render_template('6-number_template.html', n=n)
    else:
        abort(404)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """
    Route handler for the /number_odd_or_even/<n> path.

    Args:
        n (int): The value of the n variable.

    Returns:
        str: HTML page with H1 tag: "Number: n is even|odd" if n is an integer.
    """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n, parity='even' if n % 2 == 0 else 'odd')
    else:
        abort(404)

if __name__ == '__main__':
    """
    Main block to run the Flask application.

    Starts the development server on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)
