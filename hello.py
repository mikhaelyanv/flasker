from flask import Flask,render_template

# jinja 2 syntax

# safe
# capitalize
# lower
# upper
# title
# trim
# striptags



# Create app
app = Flask(__name__)

# Create a route decorator
@app.route('/')
def index():
    first_name = 'Artem'
    stuff = "This is bold text"

    favorite_pizza = ['Cheese','Pepperoni']

    return render_template('index.html',first_name = first_name, stuff = stuff , pizza = favorite_pizza)

#localhost:5000/user/name

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',user_name=name)


# Create custom error pages

# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Internal Server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500