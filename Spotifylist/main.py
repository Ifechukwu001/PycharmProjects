import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "07eed7446e8a43d2a790629a63b19fe0"
CLIENT_SECRET = "bb79151e564248f68f4270f9906cdc02"
REDIRECT_URL = "http://example.com"

date = input("What year you would like to travel to? (YYYY-MM-DD) ")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
web_content = response.text
# with open("try.html", "w", encoding="utf8") as file:
#     file.write(web_content)

# with open("try.html", encoding="utf8") as file:
#     web_content = file.read()

soup = BeautifulSoup(web_content, "html.parser")

title_list = soup.select(".o-chart-results-list-row-container #title-of-a-story")
song_names = [tag.string.strip("\n") for tag in title_list]
# print(movie_titles)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                              client_secret=CLIENT_SECRET,
                              redirect_uri=REDIRECT_URL,
                              scope="playlist-modify-private",
                              show_dialog=True,
                              cache_path="token.txt"
                              )
    )

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass
        # print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist_id)
sp.playlist_add_items(playlist_id=playlist_id["id"], items=song_uris)
