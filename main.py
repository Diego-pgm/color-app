from flask import Flask
from flask import render_template
import os

color = os.getenv('APP_COLOR')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

