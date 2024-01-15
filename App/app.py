from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/About-Me')
def about():
    return render_template("about_me.html")

if __name__ == '__main__':
    app.run(debug=True)
