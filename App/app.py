from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/About-Me', methods=['GET','POST'] )
def aboutme():
    user_input = ''
    if request.method=='POST':
        user_input = request.form.get('xss_input','')
    return render_template("about_me.html", user_input= user_input)

@app.route('/login', methods=['GET','POST'] )
def login():
    message = ''
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        query_statement = f" select username from users where username = '{username}' and password = '{password}';"

        result = db.engine.execute(query_statement)
        user = result.fetchone()
        if user:
            message = f"Welcome, {user}"
        else:
            message = "Incorrect username or password"
    return render_template('login.html', message = message)


if __name__ == '__main__':
    app.run(debug=True)
