import pandas as pd
import glob
import os

youtube_files = glob.glob("*_youtube_analytics.csv")

for y_file in youtube_files:
    game_prefix = y_file.replace("_youtube_analytics.csv", "")
    steam_file = game_prefix + "_steam_data.csv"
    combined_file = game_prefix + "_combined.csv"

    if os.path.exists(steam_file):
        try:
            df_youtube = pd.read_csv(y_file)
            df_steam = pd.read_csv(steam_file)

            for col in df_steam.columns:
                df_youtube[col] = df_steam[col].iloc[0] if not df_steam.empty else None

            df_youtube.to_csv(combined_file, index=False)
            print(f"✅ Combined saved: {combined_file}")
        except Exception as e:
            print(f"❌ Failed combining {y_file} and {steam_file}: {e}")
    else:
        print(f"⚠️ No Steam data file found for: {game_prefix}")