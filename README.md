# 🎮 Game Ecosystem Analytics App

This Streamlit app analyzes and visualizes data from YouTube and Steam to give you insights into popular games. It auto-scrapes real-time game data and lets you search, filter, and compare them easily — all in your browser.

## 🔍 Features

- Pulls top YouTube videos by game title (views, likes, comments)
- Scrapes SteamCharts data (current/peak player count)
- Merges both datasets into a searchable, sortable interface
- Automatically updates missing data on first run
- Download filtered data as CSV

## 📊 Data Sources

- [YouTube Data API v3](https://developers.google.com/youtube/v3)
- [SteamCharts (Unofficial)](https://steamcharts.com/)

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run game_analytics_app.py
