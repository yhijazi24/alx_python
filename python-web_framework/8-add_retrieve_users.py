from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alx_flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a secure key
db = SQLAlchemy(app)

# Define the User model (if not already defined)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')

            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            flash("User added successfully!", "success")
        except Exception as e:
            flash(f"Error adding user: {str(e)}", "error")

    return render_template('add_user.html')


@app.route('/users')
def display_users():
    try:
        users = User.query.all()
        return render_template('users.html', users=users)
    except Exception as e:
        flash(f"Error retrieving users: {str(e)}", "error")

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
