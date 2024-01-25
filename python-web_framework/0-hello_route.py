
from flask import Flask

"""
Create a Flask application instance.
"""
app = Flask(__name__)

"""
Define a route for the root path ('/') with strict_slashes set to False.
"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root path.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

"""
Run the application if the script is executed directly.
"""
if __name__ == '__main__':
    """
    Main block to run the Flask application.

    Starts the development server on 0.0.0.0:5000.
    """
    app.run(host='0.0.0.0', port=5000)

