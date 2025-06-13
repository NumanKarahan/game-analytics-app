# 🎮 Game Ecosystem Analytics App

This Streamlit app analyzes and visualizes data from YouTube and Steam to give you real-time insights into popular games. It auto-scrapes game stats and trending YouTube videos, and lets you search, filter, and compare them easily — all in your browser.

---

## 🔍 Features

- Pulls top YouTube videos by game title (views, likes, comments)
- Scrapes SteamCharts data (current/peak player count)
- Merges both datasets into a searchable, sortable dashboard
- Auto-updates missing data on first run
- Download filtered data as CSV

---

## 📊 Data Sources

- **YouTube Data API v3** (official)
- **SteamCharts** (unofficial scraper)

---

## 🚀 Run Locally

1. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2. **Set your YouTube API key:**
    - Create a `.env` file or set as environment variable:
        ```
        YOUTUBE_API_KEY=YOUR_API_KEY_HERE
        ```
    - Or paste your API key into `fetch_youtube_data.py` directly (not recommended for production).

3. **Fetch data:**
    ```bash
    python fetch_youtube_data.py
    python merge_youtube_steam.py
    ```

4. **Launch the app:**
    ```bash
    streamlit run app.py
    ```

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repo to GitHub (do **not** include your API keys or data files).
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and create a new app from your repo.
3. Add your YouTube API key as a secret in Streamlit Cloud.

---

## 📝 Notes

- Do **not** commit your API keys or raw data files to GitHub.
- For more games, just add their titles to your `fetch_youtube_data.py` list.
- Forks and contributions are welcome!

---
