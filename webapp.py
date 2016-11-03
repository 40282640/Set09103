from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html'), 200


@app.route('/about/')
def about():
    return render_template('about1.html'), 200

@app.route('/contact/')
def contact():
    return render_template('contact.html'), 200


if __name__ == "__main__":
    app.run(host = '0.0.0.0' , debug = True) 

