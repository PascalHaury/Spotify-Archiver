import sys
import base64
import datetime
import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import CacheFileHandler
def print_(text:str)->None:
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%d.%m.%Y - %H:%M:%S")
    print(f"[{formatted_datetime}] {text}")

def check_key_value(dictionary, key, value):
    if isinstance(dictionary, dict):
        if key in dictionary and dictionary[key] == value:
            return True
        for nested_value in dictionary.values():
            if check_key_value(nested_value, key, value):
                return True
    elif isinstance(dictionary, list):
        for item in dictionary:
            if check_key_value(item, key, value):
                return True
    return False


def download_image_and_encode(url):
    # Download the image
    response = requests.get(url)
    response.raise_for_status()

    # Encode the image in Base64
    image_data = response.content
    base64_data = base64.b64encode(image_data)
    encoded_image = base64_data.decode('utf-8')
    return encoded_image




# Spotify credentials
username = "3155ypbfxjscr5iikio7gzbgwtyy"
client_id = "81addffd52fa4b5fb9642fa2f1456025"
client_secret = "426b0028362749e7be9a57b90162c9f7"
redirect_uri = "http://localhost:8123"
scope = ["user-library-read",
         "playlist-read-private",
         "playlist-read-collaborative",
         "playlist-modify-private",
         "playlist-modify-public",
         "ugc-image-upload"]

# Playlist names
playlist_names = ["Release Radar", "Discover Weekly"]

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, username=username, open_browser=False, cache_handler=CacheFileHandler(cache_path="/SpotyBackup/cache/cachefile")))
Playlists = spotify.user_playlists(user=username)

plists = []
while Playlists:
    for playlist_raw in Playlists["items"]:
        owner = playlist_raw["owner"]["id"]
        name = playlist_raw["name"]
        plists.append(name)
        if owner == "spotify":
            if name in playlist_names:
                id = playlist_raw["id"]
                playlist = spotify.playlist(id)
                Date = playlist["tracks"]["items"][0]["added_at"]
                Name = playlist["name"]
                PlaylistDateTime = datetime.datetime.strptime(Date, '%Y-%m-%dT%H:%M:%S%z')
                PlaylistWeek = int(PlaylistDateTime.strftime("%U"))
                Playlistyear = PlaylistDateTime.year
                PlaylistMonth = PlaylistDateTime.strftime("%B")
                PlaylistImage = playlist["images"][0]["url"]
                PlaylistTracks =[]
                for trackData in playlist["tracks"]["items"]:
                    uri = trackData["track"]["uri"]
                    PlaylistTracks.append(uri)
                ArchiveName = f"{Name} {str(Playlistyear)} {PlaylistMonth} W{PlaylistWeek}"
                ArchiveDescription = f"This is the Archive of your {Name} from Week {PlaylistWeek} at {PlaylistMonth} {Playlistyear}"
                if not check_key_value(Playlists, "name", ArchiveName):
                    if ArchiveName not in plists:
                        print_(f"Create Playlist '{ArchiveName}'")
                        ArchivePlayList = spotify.user_playlist_create(user=username, name=ArchiveName, public=False, collaborative=False, description=ArchiveDescription)
                        print_(f"Add {str(len(PlaylistTracks))} songs to playlist")
                        spotify.playlist_add_items(ArchivePlayList["id"], PlaylistTracks)
                        print_(f"Add playlist image...")
                        spotify.playlist_upload_cover_image(ArchivePlayList["id"], download_image_and_encode(PlaylistImage))
                        print_(f"Change playlist to private")
                        spotify.playlist_change_details(ArchivePlayList["id"], public=False)
                        print_(f"Done!")
                    else:
                        print_(f"Playlist '{ArchiveName}' already exists")
                        if ArchiveName not in plists:
                            plists.append(ArchiveName)
                else:
                    print_(f"Playlist '{ArchiveName}' already exists")
                    if ArchiveName not in plists:
                        plists.append(ArchiveName)
            else:
                print_(f"Skip '{name}'")
    if Playlists['next']:
        Playlists = spotify.next(Playlists)
    else:
        Playlists = None
