import streamlit as st
import pandas as pd
import glob

st.set_page_config(page_title="Game Analytics Search", layout="wide")
st.title("🎮 Game Ecosystem Analytics")
st.write("Search and analyze games based on YouTube + Steam data")

# 🔁 Load all *_combined.csv files
combined_files = glob.glob("*_combined.csv")
if not combined_files:
    st.warning("No combined game files found. Run your pipeline first.")
    st.stop()

# 🧪 Choose a game
game_file = st.selectbox("Select a game:", combined_files)
df = pd.read_csv(game_file)

# 🔍 Search bar
search = st.text_input("Search YouTube video titles:", "")

# 🔽 Filter by search term
if search:
    df = df[df["Video Title"].str.contains(search, case=False, na=False)]

# 📊 Sort by selected column
sort_by = st.selectbox("Sort by:", ["Views", "Likes", "Comments", "Current Players", "24h Peak Players", "All-Time Peak Players"])
df = df.sort_values(by=sort_by, ascending=False)

# 📈 Show filtered results
st.dataframe(df, use_container_width=True)

# 📁 Download button
st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False),
    file_name=f"filtered_{game_file}",
    mime="text/csv"
)
