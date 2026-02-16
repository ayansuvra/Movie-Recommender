import streamlit as st
import pickle
import pandas as pd
import requests
import os

Files = {
    "similarity.pkl": "https://huggingface.co/ayansuvra/Movie-Recommender-System/resolve/main/similarity.pkl",
    "movies_dict.pkl": "https://huggingface.co/ayansuvra/Movie-Recommender-System/resolve/main/movies_dict.pkl"
}
def download_file(filename, url):
    if not os.path.exists(filename):
        r = requests.get(url, stream=True)
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

def req_files():
    for file, url in Files.items():
        download_file(file, url)

req_files()

st.title("Movie Recommender System")

def get_img(movie_id):
    path = poster_path(movie_id)
    img = "https://image.tmdb.org/t/p/w500"+path
    return img

def poster_path(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNDMzZDRmMTg3ODE5YmU1ZGU1NTljZjNkZDA5YTIxNSIsIm5iZiI6MTc3MTEwMTg0NC41ODIsInN1YiI6IjY5OTBkZTk0ODcwNjBhMDE2ZDEyM2Q5ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GI7jwT1x5eaQ_XRcFnkU5DaEwF3qsVJZ1VfZf3Tba4c"
    }

    response = requests.get(url, headers=headers).json()
    data = response.get('poster_path')
    return data

def recomended(movie_name):
    movie_index = movies_list_df[movies_list_df['title'] == movie_name].index[0]
    movie_id = movies_list_df[movies_list_df['title'] == movie_name].iloc[0]

    pairs = list(enumerate(similarity[movie_index].tolist()))
    pairs = sorted(pairs, key=lambda z:z[1], reverse=True)[1:11]

    recommendation_name = []
    recommendation_img = []

    for i in pairs:
       recommendation_name.append(movies_list_df.iloc[i[0]].title)
       recommendation_img.append(get_img(movies_list_df.iloc[i[0]].movie_id))

    return recommendation_name, recommendation_img

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies_list_df = pd.DataFrame(movies_dict)
movies_list = movies_list_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox(
    "Choose a Movie",
    movies_list,
    placeholder="Movies"
)


if st.button("Recommend"):
    recommendation_name, recommendation_img = recomended(selected_movie)

    cols = st.columns(4)
    for i, cols in enumerate(cols):
        with cols:
            st.text(recommendation_name[i])
            st.image(recommendation_img[i])

    cols = st.columns(4)
    for i, cols in enumerate(cols):
        with cols:
            st.text(recommendation_name[i+4])
            st.image(recommendation_img[i+4])
            cols = st.columns(4)
    cols = st.columns(4)
    for i, cols in enumerate(cols):
        if i == 2:
            break
        with cols:
            st.text(recommendation_name[i+8])
            st.image(recommendation_img[i+8])
