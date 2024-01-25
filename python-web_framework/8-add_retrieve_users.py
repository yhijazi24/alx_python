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
    # Existing code for adding a user
    # ...

    @app.route('/users')
    def display_users():
        
        @app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
        def update_user(user_id):
            user = User.query.get(user_id)
            if not user:
                flash("User not found!", "error")
                return redirect('/users')

            if request.method == 'POST':
                try:
                    name = request.form.get('name')
                    email = request.form.get('email')

                    user.name = name
                    user.email = email

                    db.session.commit()

                    flash("User updated successfully!", "success")
                    return redirect('/users')

                except Exception as e:
                    flash(f"Error updating user: {str(e)}", "error")

            return render_template('update_user.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash("User not found!", "error")
        return redirect('/users')

    if request.method == 'POST':
        try:
            db.session.delete(user)
            db.session.commit()

            flash("User deleted successfully!", "success")
            return redirect('/users')

        except Exception as e:
            flash(f"Error deleting user: {str(e)}", "error")

    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
