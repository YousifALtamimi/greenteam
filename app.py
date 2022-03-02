from flask import Flask, render_template, request
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)
# DB = SQL('sqlite:///database.db')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# main page
@app.route("/")
def index():
    return render_template("HOME.html")

@app.route("/signup", methods=["GET", "POST"])
def adduser():
    print (request)
    if request.method == "POST":
        # check if post works
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone = request.form.get("phone")

        return f'{name} {email} {surname} {phone}'
        
    return render_template("Sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("Sign_in.html")

@app.route("/about")
def about():
    return render_template("ABOUT_US.html")

@app.route("/blog")
def blog():
    return render_template("Blog.html")

@app.route("/candle")
def candle():
    return render_template("candle.html")

@app.route("/cart")
def cart():
    return render_template("Cart.html")

@app.route("/product")
def product():
    return render_template("cartproduct.html")

@app.route("/checkout")
def checkout():
    return render_template("Checkout.html")

@app.route("/contact")
def contact():
    return render_template("CONTACT.html")

@app.route("/faq")
def faq():
    return render_template("FAQ.html")

@app.route("/order-complite")
def order_complite():
    return render_template("order-complite.html")

@app.route("/plants")
def plants():
    return render_template("plants.html")

@app.route("/plastic")
def plastic():
    return render_template("plastic.html")

@app.route("/plastic2")
def plastic2():
    return render_template("plastic2.html")

@app.route("/self-care")
def self_care():
    return render_template("Self_Care.html")

@app.route("/self2")
def self2():
    return render_template("self2.html")

@app.route("/self3")
def self3():
    return render_template("self3.html")

if __name__ == '__main__':
    app.run()
