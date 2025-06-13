import requests
import pandas as pd
from bs4 import BeautifulSoup
import glob
import time

# User-agent header (some sites block "python-requests")
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Mapping: game title → Steam AppID
APP_ID_MAP = {
    "Apex Legends": "1172470",
    "Rust": "252490",
    "Counter-Strike 2": "730",
    "Grand Theft Auto V Legacy": "271590",
    "Red Dead Redemption 2": "1174180",
    "Wallpaper Engine": "431960",
    "Banana": "2923300",
    "Bongo Cat": "3419430",
    "Delta Force": "2507950"
}

def fetch_steam_stats(app_id):
    app_url = f"https://steamcharts.com/app/{app_id}"
    page = requests.get(app_url, headers=HEADERS)
    soup = BeautifulSoup(page.text, "html.parser")
    nums = soup.select("div.app-stat span.num")
    if len(nums) < 3:
        return None
    def parse_num(tag):
        text = tag.get_text(strip=True).replace(',', '')
        return int(text) if text.isdigit() else 0
    return {
        "App ID": app_id,
        "SteamCharts URL": app_url,
        "Current Players": parse_num(nums[0]),
        "24h Peak Players": parse_num(nums[1]),
        "All-Time Peak Players": parse_num(nums[2])
    }

def combine_files():
    youtube_files = glob.glob("*_youtube_analytics.csv")
    for yfile in youtube_files:
        print(f"🔄 Combining {yfile}")
        df = pd.read_csv(yfile)
        if df.empty:
            print(f"⚠️ No YouTube data in {yfile}; skipping.")
            continue
        game_title = df["Game Title"].iloc[0]
        app_id = APP_ID_MAP.get(game_title)
        if not app_id:
            print(f"⚠️ No AppID mapping for '{game_title}'. Inserting blanks.")
            stats = {
                "App ID": None,
                "SteamCharts URL": None,
                "Current Players": None,
                "24h Peak Players": None,
                "All-Time Peak Players": None
            }
        else:
            stats = fetch_steam_stats(app_id)
            if stats is None:
                print(f"⚠️ Steam stats not found for '{game_title}', inserting blanks.")
                stats = {
                    "App ID": app_id,
                    "SteamCharts URL": f"https://steamcharts.com/app/{app_id}",
                    "Current Players": None,
                    "24h Peak Players": None,
                    "All-Time Peak Players": None
                }
        # Attach stats to every row
        for key, value in stats.items():
            df[key] = value
        combined_filename = yfile.replace("_youtube_analytics.csv", "_combined.csv")
        df.to_csv(combined_filename, index=False)
        print(f"✅ Wrote combined file: {combined_filename}")
        time.sleep(1)

if __name__ == "__main__":
    combine_files()