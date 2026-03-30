from flask import render_template, url_for, flash, redirect
from flask_blog.models import Post, User
from flask_blog.forms import RegisterForm, LoginForm, PostForm
from flask_blog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def home():
    posts= Post.query.all()
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'AYour account have been created, you can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        flash('Login Unsuccessful, Please put email and Password', 'danger')
    return render_template('login.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@login_required
@app.route('/account')
def account():
    return render_template("account.html", title="Account")


@login_required
@app.route('/post/new', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        user_id = current_user.id
        post = Post(title=form.title.data, content=form.content.data, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('create_post.html', title='New Post', form=form)