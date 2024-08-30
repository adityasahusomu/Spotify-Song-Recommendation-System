# import pickle
# import streamlit as st
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
#
# CLIENT_ID = "434d65c241b94bdc92c24838dfa10543"
# CLIENT_SECRET = "7777707c730a45aea7fe9042c8d9a8dd"
#
# # initialize the spotipy client and create an object for the class
# client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
# sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
#
# def get_song_album_cover_url(song_name, artist_name):
#     search_query = f"track: {song_name} artist: {artist_name}"
#     results = sp.search(q=search_query, type='track')
#     if results and results['tracks']['items']:
#         track = results["tracks"]["items"][0]
#         album_cover_url = track["album"]["images"][0]["url"]
#         print(album_cover_url)
#         return album_cover_url
#
#     else:
#         return "https://i.postimg.cc/0QNxYz4V/social.png"
#
#
# def recommender(song_name):
#     idx = music[music['song'] == song_name].index[0]
#     distances = sorted(list(enumerate(similarity[idx])), reverse=True, key= lambda x:x[1])
#
#     recommend_music_names = []
#     recommend_music_posters = []
#     for s_id in distances[1:8]:
#         artist = music.iloc[s_id[0]].artist
#         print(artist)
#         print(music.iloc[s_id[0]].song)
#         recommend_music_posters.append(get_song_album_cover_url(music.iloc[s_id[0]].song, artist))
#         recommend_music_names.append(music.iloc[s_id[0]].song)
#     return recommend_music_names, recommend_music_posters
#
# def recommender_2(song_name):
#     idx = music2[music2['name_x'] == song_name].index[0]
#     distances = sorted(list(enumerate(similarity2[idx])), reverse=True, key= lambda x:x[1])
#
#     recommend_music_names2 = []
#     recommend_music_posters2 = []
#     for s_id in distances[1:15]:
#         artist = music2.iloc[s_id[0]].artists_final
#         print(artist)
#         print(music2.iloc[s_id[0]].name_x)
#         recommend_music_posters2.append(get_song_album_cover_url(music2.iloc[s_id[0]].name_x, artist))
#         recommend_music_names2.append(music2.iloc[s_id[0]].name_x)
#     return recommend_music_names2, recommend_music_posters2
#
#
#
# st.header('Music Recommendation System')
# music = pickle.load(open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/df_spotify_lyrics.pkl','rb'))
# similarity = pickle.load(open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/similarity_lyrics.pkl','rb'))
#
# music2 = pickle.load(open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/spotify_df_exploded_merged_genre.pkl','rb'))
# similarity2 = pickle.load(open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/similarity.pkl','rb'))
#
# music_list = music['song'].values
# music_list_2 = music2['name_x'].values
# selected_movie = st.selectbox("Type or select a song from the dropdown (Lyrics-based recommendation)", music_list)
# selected_music2 = st.selectbox("Type or select a song from the dropdown (Song scores and feature based recommendation)", music_list_2 )
#
#
#
# if st.button('Show Recommendation on the basis of lyrics'):
#     recommend_music_names, recommend_music_posters = recommender(selected_movie)
#
#     for i in range(7):
#         # Create a two-column layout
#         col1, col2 = st.columns([1, 4])  # Adjust the ratio to control the width of the image and text columns
#
#         with col1:
#             st.image(recommend_music_posters[i],
#                      use_column_width=True)  # use_column_width=True will make the image fit the column width
#         with col2:
#             st.text(recommend_music_names[i])
#
#
#
# if st.button('Show Recommendation on the basis of song features'):
#     recommend_music_names2, recommend_music_posters2 = recommender_2(selected_music2)
#
#     for i in range(14):
#         # Create a two-column layout
#         col1, col2 = st.columns([1, 4])  # Adjust the ratio to control the width of the image and text columns
#
#         with col1:
#             st.image(recommend_music_posters2[i],
#                      use_column_width=True)  # use_column_width=True will make the image fit the column width
#         with col2:
#             st.text(recommend_music_names2[i])
#
#
import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "434d65c241b94bdc92c24838dfa10543"
CLIENT_SECRET = "7777707c730a45aea7fe9042c8d9a8dd"

# Initialize the spotipy client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track: {song_name} artist: {artist_name}"
    results = sp.search(q=search_query, type='track')
    if results and results['tracks']['items']:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"


def recommender(song_name):
    idx = music[music['song'] == song_name].index[0]
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

    recommend_music_names = []
    recommend_music_posters = []
    for s_id in distances[1:8]:
        artist = music.iloc[s_id[0]].artist
        recommend_music_posters.append(get_song_album_cover_url(music.iloc[s_id[0]].song, artist))
        recommend_music_names.append(music.iloc[s_id[0]].song)
    return recommend_music_names, recommend_music_posters


def recommender_2(song_name):
    idx = music2[music2['name_x'] == song_name].index[0]
    distances = sorted(list(enumerate(similarity2[idx])), reverse=True, key=lambda x: x[1])

    recommend_music_names2 = []
    recommend_music_posters2 = []
    for s_id in distances[1:15]:
        artist = music2.iloc[s_id[0]].artists_final
        recommend_music_posters2.append(get_song_album_cover_url(music2.iloc[s_id[0]].name_x, artist))
        recommend_music_names2.append(music2.iloc[s_id[0]].name_x)
    return recommend_music_names2, recommend_music_posters2


st.header('Music Recommendation System')

# Load data and similarity matrices
music = pickle.load(open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/df_spotify_lyrics.pkl', 'rb'))
similarity = pickle.load(open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/similarity_lyrics.pkl', 'rb'))

music2 = pickle.load(
    open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/spotify_df_exploded_merged_genre.pkl', 'rb'))
similarity2 = pickle.load(open('/Users/adityasahu/Desktop/ML@Projects/MusicRecommendation/similarity.pkl', 'rb'))

# Dropdown for selecting recommendation method
recommendation_method = st.selectbox(
    "Choose recommendation method:",
    ["Show recommendation on the basis of lyrics", "Show recommendation on the basis of song scores and features"]
)

if recommendation_method == "Show recommendation on the basis of lyrics":
    music_list = music['song'].values
    selected_song = st.selectbox("Type or select a song from the dropdown (Lyrics-based recommendation)", music_list)

    if st.button('Show Recommendation on the basis of lyrics'):
        recommend_music_names, recommend_music_posters = recommender(selected_song)

        for i in range(7):
            # Create a two-column layout
            col1, col2 = st.columns([1, 4])

            with col1:
                st.image(recommend_music_posters[i], use_column_width=True)
            with col2:
                st.text(recommend_music_names[i])

elif recommendation_method == "Show recommendation on the basis of song scores and features":
    music_list_2 = music2['name_x'].values
    selected_song2 = st.selectbox(
        "Type or select a song from the dropdown (Song scores and feature based recommendation)", music_list_2)

    if st.button('Show Recommendation on the basis of song scores and features'):
        recommend_music_names2, recommend_music_posters2 = recommender_2(selected_song2)

        for i in range(14):
            # Create a two-column layout
            col1, col2 = st.columns([1, 4])

            with col1:
                st.image(recommend_music_posters2[i], use_column_width=True)
            with col2:
                st.text(recommend_music_names2[i])
