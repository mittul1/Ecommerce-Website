from flask import Flask, render_template, url_for,request, redirect, flash
from shop import app, db
from shop.forms import RegistrationForm
from shop.forms import RegistrationForm, LoginForm
from flask_login import login_required, login_user, logout_user,current_user
from shop.models import User,Item 
import flask as f
from flask_login import login_required
from shop.models import Item, User

@app.route("/")
@app.route("/home")
def home():
  items = Item.query.all()
  return render_template('home.html',items=items, user=current_user)
  return "TODO: make a shop!"

@app.route("/pricelow")
def pricelow():
	return render_template('home.html', items = Item.query.order_by('price'), title='Home')

@app.route("/pricehigh")
def pricehigh():
	return render_template('home.html', items = Item.query.order_by('price')[::-1], title='Home')

@app.route("/about")
def about():
  return render_template('about.html', title='About Me')

@app.route("/item/<int:item_id>")
def item(item_id):
  item = Item.query.get_or_404(item_id)
  return render_template('item.html',  item=item)

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful!')
    return redirect(url_for('registered'))
  return render_template('register.html',title='Register',form=form)

@app.route("/registered")
def registered():
  return render_template('registered.html', title='Thanks!')

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
      return redirect(url_for('home'))
    flash('Invalid username or password.')
    return redirect(url_for('login_error'))
  return render_template('login.html',title='Login', form=form)


@app.route("/login_error")
def login_error():
  return render_template('login_error.html', title='Login Error')

@app.route("/logout")
def logout():
  logout_user()
  flash('You\'re now logged out. Thanks for your visit!')
  return redirect(url_for('home'))

@login_required
@app.route("/cart")
def cart():
  item_ids = current_user.items
  items = []
  for item_id in item_ids:
    items.append(Item.query.get(item_id))
  return render_template('cart.html', title='Cart', items=items)

@login_required
@app.route("/add_to_cart/<int:item_id>")
def add_to_cart(item_id):
  if item_id in current_user.items:
    flash('You already have this item in your cart.')
  else:
    current_user.items.append(item_id)
    flash('Item added to cart.')
  return redirect(url_for('home'))

@login_required
@app.route("/remove_from_cart/<int:item_id>")
def remove_from_cart(item_id):
  if item_id in current_user.items:
    current_user.items.remove(item_id)
    flash('Item removed from cart.')
  return redirect(url_for('cart'))

