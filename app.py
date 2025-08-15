from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

@app.route("/", methods = ["GET"])
def home():
    query = request.args.get("q", "trending")
    params = {
        "part" : "snippet",
        "q" : query,
        "type" : "video",
        "maxResults" : 10,
        "key" : API_KEY
    }
    response = requests.get(YOUTUBE_API_URL, params=params)
    videos = response.json().get("items", [])
    return render_template("index.html", videos=videos, query=query)

if __name__ == "__main__":
    app.run(debug=True)