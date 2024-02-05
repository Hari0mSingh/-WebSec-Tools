from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
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

@app.route('/register', methods=['GET','POST'] )
def register():
    message = ''
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')

        check_query = "select username from users where username = %s"
        user_exist = db.engine.execute(check_query,(username,)).fetchone()

        if user_exist:
            insert_query = "insert into users (username, password) values(%s,%s)"
            db.engine.execute(insert_query,(username,password))

            message = "Registration successful!"
    
    return render_template("register.html",message = message)

@app.route("/redirect", methods=['GET'])
def redirect_view():
    return render_template("redirect.html")

@app.route("/open", methods=['GET'])
def open():
    target_url = request.args.get("url")
    action = request.args.get("action","redirect")

    # open redirection
    if action=="redirect":
        return redirect(target_url) #vulnerable code(open redirect)
        # return redirect("https://mysite.com") secure code 
    #ssrf
    elif action=="fetch":
        try:
            response = request.get(target_url,TimeoutError=5)
            if  response.status_code==200:
                return f"Received 200 ok {target_url}"
            else:
                return f"Received {response.status_code} from {target_url}"
        except requests.ConnectionError:
            return f"Connection refused by {target_url}"
        # except requests.ConnectTimeout:
        #     return f"Connection time out for {target_url}"
        except Exception as e:
            return str(e)
    return "Specific action and url parameters"
    
if __name__ == '__main__':
    app.run(debug=True)
