from flask import Flask, render_template, request

app = Flask(__name__)

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
    user_input = ''
    user_input_password = ''
    if request.method=='POST':
        user_input = request.form.get('username','')
        user_input_password = request.form.get('password','')
    return render_template("login.html", user_input = user_input,user_input_password = user_input_password )

if __name__ == '__main__':
    app.run(debug=True)
