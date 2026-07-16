
import time
import requests
TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMjA0MThhODI2MjZmZWY4N2M4ZTMzZGY2OWE1NmY5MyIsIm5iZiI6MTc2MDQxNzkzNS4zMjE5OTk4LCJzdWIiOiI2OGVkZDg4ZjM0Y2M1YzcwZGQ3ODU0NzkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.03ue-sRRMDGj1976GbGRYDUfE3FcG1oIYgjGRxar__M"


TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"

headers = {
    "Authorization": f"Bearer {TMDB_API_KEY}",
    "Content-Type": "application/json;charset=utf-8"
}

def get_movie_info(title, retries=3):
    params = {"query": title}

    for attempt in range(retries):
        try:
            response = requests.get(
                TMDB_SEARCH_URL,
                params=params,
                headers=headers,
                timeout=8
            )

            if response.status_code == 429:  # Too many requests
                time.sleep(1.5)
                continue

            response.raise_for_status()
            data = response.json()

            if not data["results"]:
                return None, None

            movie = data["results"][0]

            poster = movie.get("poster_path")
            summary = movie.get("overview")

            poster_url = f"https://image.tmdb.org/t/p/w500{poster}" if poster else None

            # Sleep to avoid API blocking
            time.sleep(0.3)

            return poster_url, summary

        except requests.exceptions.RequestException:
            time.sleep(1)

    return None, None
