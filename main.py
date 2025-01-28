from flask import Flask
from flask import render_template


with open('./config/web.properties', 'r') as file:
    props = [prop.strip('\n').split('=') for prop in file.readlines()]
    properties = {prop[0]: prop[1] for prop in props}

color = properties['APP_COLOR']
print(color)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

