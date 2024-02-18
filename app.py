from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return make_response("Hello, World!")

@app.route('/secretpage', methods=['GET'])
def secret():
    return make_response("This is a secret.")

app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='hw2/', 
                          prefix='hw2/', 
                          index_file='index.htm', 
                          autorefresh=True)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)