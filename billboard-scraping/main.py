import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "Your Client ID"
SPOTIFY_CLIENT_SECRET = "Your Client Secret"

# Object Creation
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.org/callback",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Surya",
    )
)

user_id = sp.current_user()["id"]

# Get User Input
past_date = input("Which year do you want to travel to? Type your date in this format YYYY-MM-DD: ")

# Billboard Request
URL = f"https://www.billboard.com/charts/hot-100/{past_date}/"
response = requests.get(url=URL)

# Get Titles using soup
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in titles]

song_uris = []
year = past_date.split("-")[0]
for song in song_titles:
    results = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exists in Spotify, Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{past_date} Billboard 100", public=False,
                                   description="Past Date top Billboard songs.")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
