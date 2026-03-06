from flask import Flask, render_template

app = Flask(__name__)

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
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)
