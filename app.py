from flask import Flask , render_template , request
import urllib
import random
import json
app = Flask(__name__)


@app.route("/")
def home():
    print("HELLO I AM A FLASK APP")
    movieName = ["Avengers" , "Avatar" , "Hello" , "Space" , "Cricket" , "Matrix"]
    myMovieName = random.choice(movieName)
    query = random.choice(["Avengers" , "Avatar" , "Hello" , "Space" , "Cricket" , "Matrix"])
    try:
        url =  f"http://www.omdbapi.com/?s={myMovieName}&apikey=70efaadb"
        response = urllib.request.urlopen(url)
        data = response.read()
        jsonData = json.loads(data)["Search"]
        return render_template("index.html" , page_name = "WOLKUS MOVIES" , movieList  = jsonData , query =query)
    except Exception as e:

        return render_template("index.html" , page_name = "WOLKUS MOVIES")


@app.route("/search" , methods = ['GET'])
# GET  - Insecure ( Search )
# POST - Secure (Password , Credit Number )
def search_results():
    movieName  =  request.args.get("Moviequery")
    movieName = movieName.strip()
    try:
        url =  f"http://www.omdbapi.com/?s={movieName}&apikey=70efaadb"
        url = url.replace(" ", "%20")
        response = urllib.request.urlopen(url)
        data = response.read()
        jsonData = json.loads(data)["Search"]
        return render_template("index.html" , page_name = "WOLKUS MOVIES" , movieList = jsonData , query = movieName)
    except Exception as e:
        print(e)
        return f"No internet connection. Please try again {e}"

app.run(debug=True)


