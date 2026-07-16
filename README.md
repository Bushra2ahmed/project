# 🎬 AI Movie Recommendation System

## 📌 Project Overview

The **AI Movie Recommendation System** is an intelligent web application that recommends movies based on a user's **mood** or **favorite actor**. It combines data filtering, mood analysis, and real-time movie information from **The Movie Database (TMDB) API** to provide personalized recommendations through an interactive Streamlit interface.

Unlike traditional recommendation systems that only recommend similar movies, this project allows users to discover movies that match their emotions or preferred actors.

---

## ✨ Features

* 😊 Mood-based movie recommendations
* 🎭 Actor-based movie recommendations
* 🎬 Real-time movie posters
* 📝 Movie summaries using TMDB API
* ⭐ IMDb ratings
* 🎨 Interactive Streamlit user interface
* ⚡ Fast recommendation engine

---

## 🎯 Objectives

* Build an AI-powered movie recommendation system.
* Recommend movies according to user emotions.
* Recommend movies featuring a selected actor.
* Integrate external APIs for richer movie information.
* Deploy an interactive web application using Streamlit.

---

## 📂 Dataset

The project uses movie metadata containing:

* Movie Title
* Genres
* IMDb Rating
* Actors
* Directors
* Movie Metadata

Additionally, the application fetches:

* Movie Posters
* Movie Overview
* Additional information

using the **TMDB API**.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit
* Requests
* TMDB API
* HTML/CSS (inside Streamlit)

---

## ⚙️ How It Works

### Mood Recommendation

The application detects the user's mood such as:

* 😊 Happy
* ❤️ Romantic
* 😢 Sad
* 😠 Angry
* 😔 Lonely

Each mood is mapped to suitable movie genres, and the highest-rated matching movies are recommended.

### Actor Recommendation

Users can also enter the name of an actor.

The application searches the movie dataset and recommends the highest-rated movies featuring that actor.

### Movie Details

For every recommended movie, the application displays:

* Movie Poster
* IMDb Rating
* Genres
* Movie Summary

using the TMDB API.

---

## 📁 Repository Structure

```text
AI-Movie-Recommendation-System/
│
├── 1app.py                 # Streamlit Application
├── recommend.py            # Recommendation Logic
├── tmdb_api.py             # TMDB API Integration
├── tmdb_5000_movies.csv      # Dataset
├── tmdb_5000_credit.csv               
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Bushra2ahmed/AI-Movie-Recommendation-System.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run 1app.py
```



---

## 💡 Skills Demonstrated

* Python Programming
* Data Analysis
* Recommendation Systems
* Streamlit Application Development
* REST API Integration
* API Handling
* User Interface Design
* Data Filtering
* Problem Solving

---

## 🚀 Future Improvements

* Content-Based Recommendation using Cosine Similarity
* Collaborative Filtering
* Personalized User Accounts
* Movie Watchlist
* Movie Trailers
* Genre-Based Recommendation
* Deep Learning Recommendation Models

---



---

## ⭐ Acknowledgement

This project was developed for learning and demonstration purposes to showcase recommendation systems, API integration, and interactive web application development using Python and Streamlit.
