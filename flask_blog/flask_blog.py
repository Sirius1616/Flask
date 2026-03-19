from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm




app = Flask(__name__)
app.config['SECRET_KEY'] = 'ae53bd80703afa7b52e730c4d0d9289b'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

posts = [
        {
            'author': 'Frank Nuel',
            'title': 'Blog post 1',
            'content': 'First post content',
            'date_posted': 'Jan 3rd 1995'

            },
        {
            'author': 'John Omo',
            'title': 'Blog post 2',
            'content': 'Second post content',
            'date_posted': 'Mar 4th 2026'
            }

        ]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'adnib@blog.com' and form.data == 'password':
            flash("You have been loggin!", 'seccess')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please putUsername and Password', 'danger')
    return render_template('login.html', title='Register', form=form)


if __name__ == "__main__":
    app.run(debug=True)
