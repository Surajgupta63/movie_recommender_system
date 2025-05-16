<<<<<<< HEAD
import pickle
import requests
import streamlit as st
from bs4 import BeautifulSoup


movies = pickle.load(open("movies_data.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movie_names = movies['movie_name'].values

st.title("Movie Recommender System")

def recommend_movies(movie):
    movie_index = movies[movies['movie_name'] == movie].index[0]
    distances   = similarity[movie_index]
    top_movies  = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:4]
    top3        = []
    movie_ids    = []
    for i in top_movies:
        top3.append(movies.iloc[i[0]].movie_name)
        movie_ids.append(movies.iloc[i[0]].movie_id)
    return top3, movie_ids

selected_movie = st.selectbox("Choose Your Movie", movie_names)
if st.button("Recommend"):
    top_movies, movie_ids = recommend_movies(selected_movie)

    for i in range(len(top_movies)):
       
        # data = response.json()
        st.text(top_movies[i])
=======
import pickle
import streamlit as st


movies = pickle.load(open("movies_data.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movie_names = movies['movie_name'].values

st.title("Movie Recommender System")

def recommend_movies(movie):
    movie_index = movies[movies['movie_name'] == movie].index[0]
    distances   = similarity[movie_index]
    top_movies  = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:4]
    top3        = []
    movie_ids    = []
    for i in top_movies:
        top3.append(movies.iloc[i[0]].movie_name)
        movie_ids.append(movies.iloc[i[0]].movie_id)
    return top3, movie_ids

selected_movie = st.selectbox("Choose Your Movie", movie_names)
if st.button("Recommend"):
    top_movies, movie_ids = recommend_movies(selected_movie)

    for i in range(len(top_movies)):
        st.text(top_movies[i])
>>>>>>> 67341386c790a097a178a7e05f2fa29ac676954f
