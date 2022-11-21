from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import *
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
import os
import re
import MySQLdb.cursors


#If using xampp the app should be in htdocs


# from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key = "xyz"
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pumpkin'
 
mysql = MySQL(app)

PLANTS = ['Aloe Vera', 'Peace Lily', 'Lemon Tree']
# REGISTRANTS = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
      return render_template("greet.html")

#Login method for Flask Python
#Change accounts table to users, username and password dont change, no encryption
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = 'Enter user details here'
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            # session['id'] = user['id']
            session['username'] = user['username']
            session['password'] = user['password']
            session['email'] = user['email']
            msg = 'Logged in successfully !'
            return redirect(url_for('profile'))
            # return render_template('profile.html', username=current_user.username)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/profile')
def profile():
    return render_template('profile.html', plantTypes=PLANTS, username=session['username'],  password=session['password'], email=session['email'])

@app.route('/logout')
# @flask_login.login_required
def logout():
    # logout_user()
    session.pop('loggedin', None)
    # session.pop('id', None)
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = % s', (username, ))
        user = cursor.fetchone()
        if user:
            msg = 'Account already exists !'
            return redirect(url_for('login'))
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', (name, username, password, email,))
            mysql.connection.commit()
            cursor.close()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route("/dashboard", methods=["GET"])
# @flask_login.login_required
def dashboard():
    return render_template("dashboard.html", username=session['username'])

@app.route("/new_plant", methods=["GET", "POST"])
# @flask_login.login_required
def new_plant():
    # if request.method == "GET":
    msg = ''
    username=session['username']

    if request.method == "POST":
        plantName = request.form['plantName']
        if not plantName:
            return render_template('error.html', message="Missing plant name")        
        
        plantType = request.form['plantType']
        if not plantType:
            return render_template('error.html', message="Missing plant type")
        
        cur1 = mysql.connection.cursor()
        cur1.execute("select Id from users where username = %s", (username, ))
        userId = cur1.fetchone()
        
        cursor = mysql.connection.cursor()
        cursor.execute('''insert into inventary values (NULL, %s, %s, %s)''', (userId, plantName, plantType))
        mysql.connection.commit()
        cursor.close()
        msg = 'You have successfully registered a new plant !'
        return redirect(url_for('myplant'))

    return render_template("new_plant.html", msg = msg, username=session['username'], plantTypes=PLANTS)

@app.route("/myplant", methods=["GET", "POST"])
# @flask_login.login_required
def myplant():

    username=session['username']
    
    #select user id
    cur1 = mysql.connection.cursor()
    cur1.execute("select Id from users where username = %s", (username, ))
    userId = cur1.fetchone()

    #obtain all the plants for a user
    cur2 = mysql.connection.cursor()
    cur2.execute("select * from inventary where userId = %s", (userId, ))
    inventary = cur2.fetchall()

    #obtain the plant Id 
    cur3 = mysql.connection.cursor()
    cur3.execute("select id from inventary where userId = %s", (userId,))
    plantId = cur3.fetchone()

    # select the specific plant for each user
    cur4 = mysql.connection.cursor()
    cur4.execute("select *, max(date) from eventsdht11 where idPlant = %s", (plantId,))
    plantData = cur4.fetchall()

    
    return render_template("myplant.html", username=session['username'], inventary=inventary, plantData=plantData)


@app.route("/plant_info", methods=["GET", "POST"])
def plant_info():
    username=session['username']
    
    #select user id
    cur5 = mysql.connection.cursor()
    cur5.execute("select Id from users where username = %s", (username, ))
    userId = cur5.fetchone()

    #obtain all the plants for a user
    cur6 = mysql.connection.cursor()
    cur6.execute("select * from inventary where userId = %s", (userId, ))
    inventary = cur6.fetchall()

    #obtain the plant Id 
    cur7 = mysql.connection.cursor()
    cur7.execute("select id from inventary where userId = %s", (userId,))
    plantId = cur7.fetchone()

    # select the specific plant for each user
    cur8 = mysql.connection.cursor()
    cur8.execute("select *  from eventsdht11 where idPlant = %s", (plantId,))
    newPlantData = cur8.fetchall()

    
    return render_template("plant_info.html", username=session['username'], inventary=inventary, newPlantData=newPlantData)

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
        
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    app.debug = True
    app.run()
