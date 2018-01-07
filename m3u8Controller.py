from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def root():
    name = 'Hello world'
    return render_template('hello.html', title='flask_test', name=name)


if __name__ == "__main__":
    app.run(debug=True)
