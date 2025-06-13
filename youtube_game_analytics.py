import pandas as pd
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# --- 1. CONFIG ---
API_KEY = "AIzaSyBj1oBM7VG7pPrbEtJn604DULz7AiDoaTY"  # 👈 Replace with your real key
GAME_TITLE = "Red Dead Redemption 2"              # 👈 Change to test other games
MAX_RESULTS = 20

# --- 2. INIT YOUTUBE API ---
youtube = build("youtube", "v3", developerKey=API_KEY)

# --- 3. DATE RANGE (last 30 days) ---
today = datetime.utcnow()
last_month = today - timedelta(days=30)
published_after = last_month.isoformat("T") + "Z"

# --- 4. SEARCH VIDEOS ---
search_response = youtube.search().list(
    q=GAME_TITLE,
    part="snippet",
    type="video",
    order="viewCount",
    publishedAfter=published_after,
    maxResults=MAX_RESULTS
).execute()

# --- 5. PROCESS VIDEOS ---
video_data = []

for item in search_response["items"]:
    video_id = item["id"]["videoId"]
    title = item["snippet"]["title"]
    channel = item["snippet"]["channelTitle"]
    published_at = item["snippet"]["publishedAt"]

    stats = youtube.videos().list(part="statistics", id=video_id).execute()
    stats_item = stats["items"][0]["statistics"]

    video_data.append({
        "Game Title": GAME_TITLE,
        "Video Title": title,
        "Channel": channel,
        "Published At": published_at,
        "Views": int(stats_item.get("viewCount", 0)),
        "Likes": int(stats_item.get("likeCount", 0)),
        "Comments": int(stats_item.get("commentCount", 0)),
        "Video ID": video_id,
        "Video URL": f"https://www.youtube.com/watch?v={video_id}"
    })

# --- 6. SAVE TO CSV ---
df = pd.DataFrame(video_data)
filename = f"{GAME_TITLE.lower().replace(' ', '_')}_youtube_analytics.csv"
df.to_csv(filename, index=False)

print(f"✅ Data saved to: {filename}")
