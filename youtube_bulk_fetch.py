import os
import time
import pandas as pd
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone

YOUTUBE_API_KEY = "YourAPIKEY"
youtube = build("youtube", "v3", developerKey="YourAPIKEY")

games = [
    "Apex Legends",
    "Banana",
    "Counter-Strike 2",
    "Bongo Cat",
    "Delta Force",
    "Grand Theft Auto V Legacy",
    "Rust",
    "Wallpaper Engine"
]

def fetch_youtube_data(game_title):
    print(f"🔍 Fetching data for: {game_title}")
    published_after = (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

    search_response = youtube.search().list(
        q=game_title,
        type="video",
        part="id,snippet",
        maxResults=20,
        order="viewCount",
        publishedAfter=published_after
    ).execute()

    videos = []
    for item in search_response.get("items", []):
        video_id = item["id"]["videoId"]
        snippet = item["snippet"]

        stats_response = youtube.videos().list(
            part="statistics",
            id=video_id
        ).execute()

        statistics = stats_response["items"][0]["statistics"] if stats_response["items"] else {}

        videos.append({
            "Game Title": game_title,
            "Video ID": video_id,
            "Title": snippet["title"],
            "Channel": snippet["channelTitle"],
            "Published At": snippet["publishedAt"],
            "Views": int(statistics.get("viewCount", 0)),
            "Likes": int(statistics.get("likeCount", 0)) if "likeCount" in statistics else None,
            "Comments": int(statistics.get("commentCount", 0)) if "commentCount" in statistics else None
        })
        time.sleep(1)

    df = pd.DataFrame(videos)
    if not df.empty:
        filename = game_title.lower().replace(" ", "_") + "_youtube_analytics.csv"
        df.to_csv(filename, index=False)
        print(f"✅ Saved: {filename}")
    else:
        print(f"⚠️ No videos found for: {game_title}")

# Run for all games
for game in games:
    try:
        fetch_youtube_data(game)
    except Exception as e:
        print(f"❌ Failed for {game}: {e}")
    time.sleep(2)
