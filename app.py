from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# from datetime import timedelta

app = Flask(__name__)
from reading_pictures import *

app.register_blueprint(index_reading_pictures)
from stylepro_artistic import *

app.register_blueprint(index_stylepro_artistic)

Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/error', methods=['POST', 'GET'])
def error():
    return render_template('404.html')


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8080, debug=True,
            ssl_context=("4543112_www.livingbody.xyz.pem", "4543112_www.livingbody.xyz.key"))
