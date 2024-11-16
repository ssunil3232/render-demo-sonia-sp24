from flask import *
from whitenoise import WhiteNoise

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template("home.html")

app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='project1/', 
                          prefix='/tswift-discography/', 
                          index_file='index.htm', 
                          autorefresh=True)

app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='project2/', 
                          prefix='/yelp-pittsburgh/', 
                          index_file='index.htm', 
                          autorefresh=True)

app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='project3/', 
                          prefix='/under-the-covers/', 
                          index_file='intro.htm', 
                          autorefresh=True)

app.wsgi_app = WhiteNoise(app.wsgi_app, 
                          root='project3/', 
                          prefix='/under-the-covers/article/', 
                          index_file='index.htm', 
                          autorefresh=True)


if __name__ == "__main__":
    app.run(threaded=True, port=5000)