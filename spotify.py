import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

# SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI set as environmental variables

user_id = "21ozahrkhnk47leielel36bfq"
scope = "user-library-read playlist-modify-public"

token = util.prompt_for_user_token(user_id, scope)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Playlist details
playlist_name = "NYE Bangers"
playlist_desc = "A playlist for the last day of the year. Created using the Spotify Web API in Python"

playlists = sp.user_playlists(user_id)

# Create empty playlist
def create_playlist():
    playlist_names = []

    for i in playlists["items"]:
        playlist_names.append(i["name"])

    if playlist_name not in playlist_names:
        sp.user_playlist_create(
            user_id,
            playlist_name,
            description=playlist_desc,
        )

    global new_playlists

    new_playlists = sp.user_playlists(user_id)


# Get track recommendations
def get_track_recommendations():
    song1_id = "3lUQpvfWFcxZC3RYAVGE7F"  # Pink Sweat$ - I Feel Good
    song2_id = "4aHrviUXxabPdIgWxdYQLt"  # Fiji Blue - Butterflies
    song3_id = "5HCyWlXZPP0y6Gqq8TgA20"  # The Kid LAROI, Justin Bieber - STAY
    song4_id = "4Gt2kh3QbAGU6yquOWn4aW"  # Lauv, Conan Gray - Fake
    song5_id = "3gwoz4xZuye0agjYgrC2je"  # Troye Sivan - Easy

    seed_tracks = [song1_id, song2_id, song3_id, song4_id, song5_id]

    recommendations = sp.recommendations(
        seed_tracks=seed_tracks,
        country="GB",
        limit=100,
        min_danceability=0.7,
        min_energy=0.5,
        max_instrumentalness=0.3,
        min_valence=0.5,
    )

    global track_id

    track_id = [track["id"] for track in recommendations["tracks"]]


# Add songs to playlist/ Replace songs in playlist
def add_to_playlist():
    for i in new_playlists["items"]:
        if i["name"] == playlist_name:
            sp.user_playlist_replace_tracks(user_id, i["id"], track_id)
            break


# Main function
def main():
    create_playlist()
    get_track_recommendations()
    add_to_playlist()


if __name__ == "__main__":
    main()
