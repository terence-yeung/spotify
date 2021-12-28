import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

user_id = "21ozahrkhnk47leielel36bfq"
scope = "user-library-read playlist-modify-public"

token = util.prompt_for_user_token(user_id, scope)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Playlist details
playlist_name = "Feel Good Tunes"
playlist_desc = "A good mood playlist created using the Spotify Web API in Python"


# Create empty playlist
def create_playlist():
    sp.user_playlist_create(
        user_id,
        playlist_name,
        description=playlist_desc,
    )


# Get track recommendations
def get_track_recommendations():
    song1_id = "3lUQpvfWFcxZC3RYAVGE7F"  # Pink Sweat$ - I Feel Good
    song2_id = "4aHrviUXxabPdIgWxdYQLt"  # Fiji Blue - Butterflies
    song3_id = "2xWaMntwciToo1CbOxWmbX"  # wave to earth - light
    song4_id = "21fmk5RzKY0lQyyX1i64Xw"  # ØZI - hair tie
    song5_id = "4MOUAKzdy6wa2AJHuuxIi8"  # Majid Jordan - Summer Rain

    seed_tracks = [song1_id, song2_id, song3_id, song4_id, song5_id]

    recommendations = sp.recommendations(
        seed_tracks=seed_tracks,
        country="GB",
        limit=50,
        min_energy=0.3,
        max_energy=0.8,
        max_instrumentalness=0.3,
        min_valence=0.5,
    )

    global track_id

    track_id = [track["id"] for track in recommendations["tracks"]]


# Add to playlist
def add_to_playlist():
    playlists = sp.user_playlists(user_id)
    for i in playlists:
        if playlists["items"][0]["name"] == playlist_name:
            playlist_id = playlists["items"][0]["id"]
            break

    sp.playlist_add_items(playlist_id, track_id)


# Full function
def main():
    create_playlist()
    get_track_recommendations()
    add_to_playlist()


if __name__ == "__main__":
    main()
