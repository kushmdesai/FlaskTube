from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


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

@app.route("/suggest")
def suggest():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])
    
    url = f"https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={query}"
    r = requests.get(url)

    if r.status_code != 200:
        return jsonify([])

    data = r.json()
    suggestions = data[1]
    return jsonify(suggestions)

@app.route("/related/<video_id>")
def related_videos(video_id):
    # First, get the video details to find the channelId
    video_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={API_KEY}"
    video_res = requests.get(video_url).json()

    if "items" not in video_res or len(video_res["items"]) == 0:
        return jsonify([])  # Video not found

    channel_id = video_res["items"][0]["snippet"]["channelId"]

    # Now, fetch the latest videos from the same channel
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&type=video&maxResults=10&key={API_KEY}"
    search_res = requests.get(search_url).json()

    videos = []
    for item in search_res.get("items", []):
        # Skip the current video itself
        if item["id"]["videoId"] == video_id:
            continue
        videos.append({
            "videoId": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
            "channel": item["snippet"]["channelTitle"]
        })

    return jsonify(videos)

if __name__ == "__main__":
    app.run(debug=True)