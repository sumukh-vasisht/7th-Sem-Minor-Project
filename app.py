# plotting graph here
import pandas as pd

test = pd.read_csv('test.csv', names=['A', 'B', 'C', 'D'])
fig = test.plot.line().get_figure()
fig.savefig('static/images/plot.png')

# app here
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)