from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route handler for the root path.

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    This script runs a simple Flask web application.

    The application listens on 0.0.0.0, port 5000, and has a single route:
    - Route '/': Displays the message "Hello HBNB!" when accessed.

    To run the application, execute this script.

    Example:
        python3 0-hello_route.py
    """
    # Start the Flask development server on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
