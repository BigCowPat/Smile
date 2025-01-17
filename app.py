from flask import Flask, render_template, request, session, redirect
import sqlite3
from sqlite3 import Error
DB_NAME = "smile.db"

app = Flask(__name__)
app.secret_key = "b347fi34p9ygd23g7g2379xhj92p3hg4yz879r3dg8fi90243669420"

def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return None


@app.route('/')
def render_homepage():
    return render_template("home.html")

@app.route('/menu' )
def render_menu():

    con = create_connection(DB_NAME)

    query = "SELECT name, description, volume, image, price FROM product"

    cur = con.cursor()
    cur.execute(query)
    product_list = cur.fetchall()
    con.close()

    return render_template("menu.html", products=product_list)

@app.route('/contact')
def render_contact():
    return render_template("contact.html")

@app.route('/login' methods=['GET','POST'])
def render_login():
    if request.method == 'POST':
        email = request.form['email'].lower().strip()
        password1 = request.form['password1'].strip()

        query = """SELECT id, fname, password FROM customer WHERE email = ?"""
        con = create_connection(DB_NAME)
        cur = con.cursor()
        cur.execute(query, (email,))
        user_data = cur.fetchall()
        con.close()

        try:
            userid = user_data[0][0]
            firstname = user_data[0][1]
            db_password = user_data[0][2]
        except IndexError:
            return redirect("login?error=Email+invaild+or+password+incorrect")

    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def render_signup():
    if request.method == 'POST':
        print(request.form)
        fname = request.form.get("fname").strip().title()
        lname = request.form.get("lname").strip().title()
        email = request.form.get("email").strip().lower()
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if password1 != password2:
            return redirect('/signup?error=Passwords+dont+match')
        if len(password1) < 8:
            return redirect('/signup?error=Password+too+short')

        con = create_connection(DB_NAME)

        query = "INSERT INTO customer(id, fname, lname, email, password) VALUES(NULL,?,?,?,?)"

        cur = con.cursor()  # I need this line next
        try:
            cur.execute(query, (fname, lname, email, password1)) #this line executes the query
        except sqlite3.IntegrityError:
            return redirect('signup?=error+Email+is+already+used')
        con.commit()
        con.close()
        return redirect('/login')

    return render_template("signup.html")
app.run(host="0.0.0.0")
