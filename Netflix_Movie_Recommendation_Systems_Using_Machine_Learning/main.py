import streamlit as st
import  pickle
import  pandas as pd
import  requests
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def fetch_poster(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    # print(data)
    # st.text(data)
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        id = movies.iloc[i[0]].id
        recommended_movies_poster.append(fetch_poster(id))
        recommended_movies.append(movies.iloc[i[0]].original_title)
    return recommended_movies,recommended_movies_poster
        # print(i[0])

# Define a layout with two columns
col_1, col_2 = st.columns([1, 4])

# In the first column (col1), add the Netflix logo
with col_1:
    st.image("nt.png", width=200)

# In the second column (col2), add the title with CSS padding
with col_2:
    st.markdown(
        "<h2 style='padding: 40px 0px 0px 60px;'>Netflix Movie Recommendation System</h2>",
        unsafe_allow_html=True,
    )

# Create a simple recommendation system
st.subheader('Discover Your Next Movie Favorite')

# User selects a movie
movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Create two rows of 4 columns each
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)

    # Display recommendations in the first row
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], width=150)
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], width=150)
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], width=150)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], width=150)

    # Display recommendations in the second row
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], width=150)
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5], width=150)
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6], width=150)
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7], width=150)

