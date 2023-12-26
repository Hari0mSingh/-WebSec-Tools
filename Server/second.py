from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

# @app.route('/page/<int:number>')
# def bye(number):
#     return f"This is page {number}"

@app.route('/page/<name>')
def bye(name):
    return f"Welcome {name} to our page"

if __name__ == "__main__":
    app.run(debug=True)
