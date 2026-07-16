import streamlit as st
from recommend import recommend_movies
from tmdb_api import get_movie_info

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
.movie-card {
    background-color: #111;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0px 0px 10px rgba(255,255,255,0.05);
}
.movie-title {
    font-size: 26px;
    font-weight: bold;
    color: #ff4b4b;
}
.rating {
    background-color: #ffcc00;
    padding: 5px 10px;
    border-radius: 10px;
    font-weight: bold;
    color: black;
    display: inline-block;
}
.genre {
    color: #00e5ff;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("🎥 Movie Recommender AI")
st.sidebar.info(
    "🔍 Enter:\n"
    "- A **mood** (happy, sad, romantic)\n"
    "- An **actor name** (Tom Cruise, SRK)\n\n"
    "📽 Powered by ML + TMDB API"
)

# ------------------ MAIN TITLE ------------------
st.title("🎬 AI Movie Recommendation System")
st.caption("Get movie recommendations based on **Mood** or **Actor Name**")

# ------------------ INPUT ------------------
user_input = st.text_input(
    "✨ Enter Mood or Actor Name",
    placeholder="e.g. happy, sad, romantic OR Leonardo DiCaprio"
)

# ------------------ BUTTON ------------------
if st.button("🎯 Recommend Movies"):
    if not user_input.strip():
        st.warning("⚠ Please enter a mood or actor name.")
    else:
        with st.spinner("🎬 Finding the best movies for you..."):
            mode, mood, movies = recommend_movies(user_input)

        if movies is None or movies.empty:
            st.error("❌ No movies found. Try another mood or actor.")
        else:
            if mode == "mood":
                st.success(f"🎭 Detected Mood: **{mood.capitalize()}**")

            st.subheader("🍿 Recommended Movies")

            for _, row in movies.head(5).iterrows():
                title = row["movie_title"]
                imdb = row["imdb_score"]
                genres = row["genres"]

                poster, summary = get_movie_info(title)

                st.markdown('<div class="movie-card">', unsafe_allow_html=True)
                st.markdown(f'<div class="movie-title">🎥 {title}</div>', unsafe_allow_html=True)

                col1, col2 = st.columns([1, 3])

                with col1:
                    if poster:
                        st.image(poster, use_column_width=True)
                    else:
                        st.info("No poster available")

                with col2:
                    st.markdown(f'<span class="rating">⭐ IMDB: {imdb}</span>', unsafe_allow_html=True)
                    st.write("")
                    st.markdown(f'🎭 <span class="genre">{genres}</span>', unsafe_allow_html=True)
                    st.write("")
                    st.markdown("📝 **Summary**")
                    st.write(summary if summary else "No summary available.")

                st.markdown("</div>", unsafe_allow_html=True)
