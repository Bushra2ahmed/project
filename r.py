import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================
# LOAD DATASET
# ==========================
df = pd.read_csv("movie_metadata.csv")

# ==========================
# DATA CLEANING
# ==========================
df["genres"] = df["genres"].astype(str)
df["movie_title"] = df["movie_title"].astype(str).str.strip()
df["actor_1_name"] = df["actor_1_name"].astype(str)
df["actor_2_name"] = df["actor_2_name"].astype(str)
df["actor_3_name"] = df["actor_3_name"].astype(str)

# Drop rows with missing IMDB score
df = df.dropna(subset=["imdb_score"])

# ==========================
# CREATE TAGS (CONTENT-BASED)
# ==========================
df["tags"] = (
    df["genres"] + " " +
    df["actor_1_name"] + " " +
    df["actor_2_name"] + " " +
    df["actor_3_name"]
).str.lower()

# ==========================
# TF-IDF FOR MOVIES
# ==========================
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["tags"])

# Cosine similarity matrix
similarity = cosine_similarity(tfidf_matrix)

# ==========================
# NLP-BASED MOOD DETECTION
# ==========================
mood_texts = {
    "happy": "happy joyful excited cheerful energetic fun",
    "sad": "sad depressed emotional heartbroken crying upset",
    "angry": "angry furious mad violent aggressive annoyed irritated",
    "romantic": "romantic love affection relationship couple",
    "lonely": "lonely alone isolated empty silent",
    "bored": "bored nothing tired dull boring",
    "stressed": "stress tense anxious worried"

}

mood_vectorizer = TfidfVectorizer(stop_words="english")
mood_vectors = mood_vectorizer.fit_transform(mood_texts.values())

def detect_mood(user_text):
    user_text = user_text.lower()
    user_vec = mood_vectorizer.transform([user_text])
    scores = cosine_similarity(user_vec, mood_vectors)

    best_idx = scores.argmax()
    best_score = scores[0][best_idx]

    if best_score < 0.15:
        return None

    return list(mood_texts.keys())[best_idx]

# ==========================
# MOOD → GENRE MAPPING
# ==========================
mood_to_genre = {
    "happy": ["Comedy", "Adventure", "Family"],
    "sad": ["Drama", "Biography"],
    "angry": ["Action", "Thriller"],
    "romantic": ["Romance", "Drama"],
    "lonely": ["Drama", "Family"],
    "bored": ["Adventure" , "Fantasy" ],
    "stressed": ["Calm" ,"Drama"]
}

# ==========================
# MAIN RECOMMENDATION FUNCTION
# ==========================
def recommend_movies(user_input):

    text = user_input.lower()

    # 1️⃣ MOOD BASED RECOMMENDATION
    mood = detect_mood(text)
    if mood:
        genres = mood_to_genre[mood]
        filtered = df[df["genres"].str.contains("|".join(genres), case=False, na=False)]
        filtered = filtered.sort_values("imdb_score", ascending=False)
        return "mood", mood, filtered[["movie_title", "genres", "imdb_score"]].head(5)

    # 2️⃣ ACTOR BASED RECOMMENDATION
    actor_filtered = df[
        (df["actor_1_name"].str.contains(text, case=False, na=False)) |
        (df["actor_2_name"].str.contains(text, case=False, na=False)) |
        (df["actor_3_name"].str.contains(text, case=False, na=False))
    ]

    if not actor_filtered.empty:
        actor_filtered = actor_filtered.sort_values("imdb_score", ascending=False)
        return "actor", user_input.title(), actor_filtered[["movie_title", "genres", "imdb_score"]].head(5)

    # 3️⃣ MOVIE BASED (TF-IDF SIMILARITY)
    normalized_input = text.replace(" ", "").replace("-", "")
    titles = df["movie_title"].str.lower().str.replace(" ", "").str.replace("-", "")

    if normalized_input in titles.values:
        idx = titles[titles == normalized_input].index[0]

        sim_scores = list(enumerate(similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        movie_indices = [i[0] for i in sim_scores[1:6]]
        result = df.iloc[movie_indices]

        return "movie", df.iloc[idx]["movie_title"], result[["movie_title", "genres", "imdb_score"]]

    return "none", None, None

# ==========================
# TESTING (CLI MODE)
# ==========================
if __name__ == "__main__":
    while True:
        user_input = input("\nEnter mood / actor / movie (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        mode, key, recommendations = recommend_movies(user_input)

        if mode == "none":
            print("❌ No recommendation found.")
        else:
            print(f"\n🔍 Recommendation Type: {mode.upper()} ({key})")
            print(recommendations.to_string(index=False))
