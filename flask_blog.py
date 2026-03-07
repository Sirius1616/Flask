from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'ae53bd80703afa7b52e730c4d0d9289b'

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


@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('register.html', title='Register', form=form)


if __name__ == "__main__":
    app.run(debug=True)
