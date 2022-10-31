from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = '08wuov8m3y5tghvoujkldjdhiosejyrthiusn3cmohas4i5rjoliwkzdvb'


@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html')


if __name__ == '__main__':
    app.run(debug=True)