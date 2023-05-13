import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=afa00928b041968b39d096efe1822eb9&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]


    Recommended_movies = []
    Recommended_movies_posters = []
    for i in movies_list:
       movie_id = movies.iloc[i[0]].movie_id
       Recommended_movies.append(movies.iloc[i[0]].title)
       # fetch poster from api
       Recommended_movies_posters.append(fetch_poster(movie_id))
    return Recommended_movies,Recommended_movies_posters

movies_ldict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_ldict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

Selected_movie_name = st.selectbox(
'Which movie do you like best?',
movies['title'].values)

if st.button('Show Recommendation'):
    Recommended_movie_names,Recommended_movie_posters = Recommend(Selected_movie_name)
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(Recommended_movie_names[0])
        st.image(Recommended_movie_posters[0])
    with col2:
        st.text(Recommended_movie_names[1])
        st.image(Recommended_movie_posters[1])

    with col3:
        st.text(Recommended_movie_names[2])
        st.image(Recommended_movie_posters[2])
    with col4:
        st.text(Recommended_movie_names[3])
        st.image(Recommended_movie_posters[3])
    with col5:
        st.text(Recommended_movie_names[4])
        st.image(Recommended_movie_posters[4])