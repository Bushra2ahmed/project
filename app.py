import streamlit as st
from recommend  import recommend_movies
from tmdb_api import  get_movie_info

st.set_page_config(page_title="Movie Recommendation AI", page_icon="🎬")

st.title("🎬 AI Movie Recommender")
st.write("Type a mood or actor name below ⬇")

user_input = st.text_input("Enter mood or actor name")

if st.button("Recommend"):
    if not user_input.strip():
        st.warning("Please enter mood or actor name.")
    else:
        mode, mood, movies = recommend_movies(user_input)[:5]

        if mode == "actor" and movies is None:
            st.error("❌ No movies found for this actor.")
        else:
            if mode == "mood":
                st.subheader(f"Detected Mood: **{mood.capitalize()}** 🎭")
                st.write("Here are your movie recommendations:")

            for _, row in movies.iterrows():
                title = row["movie_title"]
                imdb = row["imdb_score"]
                genres = row["genres"]

                poster, summary = get_movie_info(title)

                st.markdown(f"## 🎥 {title}")

                col1, col2 = st.columns([1, 3])
                with col1:
                    if poster:
                        st.image(poster, width=150)
                    else:
                        st.write("No poster available")

                with col2:
                    st.write(f"⭐ **IMDB Rating:** {imdb}")
                    st.write(f"🎭 **Genres:** {genres}")
                    st.write("📝 **Summary:**")
                    st.write(summary)

                st.markdown("---")
