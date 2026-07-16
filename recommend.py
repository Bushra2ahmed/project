import pandas as pd

# Load dataset
df = pd.read_csv("movie_metadata.csv")

# Cleaning
df["genres"] = df["genres"].astype(str)
df["movie_title"] = df["movie_title"].astype(str)
df["actor_1_name"] = df["actor_1_name"].astype(str)
df["actor_2_name"] = df["actor_2_name"].astype(str)
df["actor_3_name"] = df["actor_3_name"].astype(str)

# --------------------------
# MOOD DETECTION
# --------------------------
def detect_mood(text):
    text = text.lower()

    mood_keywords = {
        "happy": ["happy", "joy", "excited", "glad"],
        "sad": ["sad", "depressed", "heartbroken"],
        "angry": ["angry", "furious", "mad"],
        "romantic": ["love", "romantic", "affection"],
        "lonely": ["lonely", "alone", "isolated"],
    }

    for mood, words in mood_keywords.items():
        for w in words:
            if w in text:
                return mood
    return None

# --------------------------
# MOOD → GENRE MAPPING
# --------------------------
mood_to_genre = {
    "happy": ["Comedy", "Adventure", "Family"],
    "sad": ["Drama", "Biography"],
    "angry": ["Action", "Thriller"],
    "romantic": ["Romance", "Drama"],
    "lonely": ["Family", "Drama", "Friendship"]
}

# --------------------------
# MAIN RECOMMENDER FUNCTION
# --------------------------
def recommend_movies(text):
    text_low = text.lower()
    mood = detect_mood(text)

    # If mood found
    if mood:
        genres = mood_to_genre[mood]
        filtered = df[df["genres"].str.contains("|".join(genres), case=False)]
        filtered = filtered.sort_values(by="imdb_score", ascending=False)
        return "mood", mood, filtered.head(5)

    # Otherwise treat input as actor name
    filtered = df[
        df["actor_1_name"].str.lower().str.contains(text_low) |
        df["actor_2_name"].str.lower().str.contains(text_low) |
        df["actor_3_name"].str.lower().str.contains(text_low)
    ]

    if filtered.empty:
        return "actor", None, None

    filtered = filtered.sort_values(by="imdb_score", ascending=False)
    return "actor", None, filtered.head(5)

# Test
recommend_movies("I am feeling happy")
recommend_movies("Leonardo DiCaprio")
