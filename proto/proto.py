import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

scope=""
sp=None

def get_all_user_playlists()->list:
    """Can rework this to filter down to only the information we want to use locally"""
    playlists=[]
    chunk_size = 50 # max size
    page = sp.current_user_playlists(limit=chunk_size)
    next = page["next"]
    while next:
        next = page["next"]
        for i, playlist in enumerate(page["items"]):
            playlists.append(playlist["name"])
        page = sp.next(page)
    return playlists

def search_for_user_playlist(name:str):
    result = sp.search(name, type="playlist")
    for playlist in result['playlists']['items']:
        if playlist["owner"]["id"]==current_user["id"]:
            return playlist
    
    print("Playlist not found by that name, did you mean...")
    # TODO: Find most similar 5 names
    print("Owned playlist similarity not implemented, deferring to playlist browse")
    return scroll_user_playlists()
    #pprint.pprint(result)

def scroll_user_playlists():
    chunk_size = 15
    page = sp.current_user_playlists(limit=chunk_size)
    next = page["next"]
    count = 0
    while next:
        print(f"{count}-{min(count + chunk_size,page['total'])} of {page['total']}")
        print("-------------")
        for i, playlist in enumerate(page["items"]):
            print(i, playlist["name"])
        choice = input("Choose a playlist by number, leave empty for next page: ")
        if choice != "":
            return playlist
        count += i+1
        page = sp.next(page)
        print("--------------")
    print("Reached end of your playlists, aborting. ")
    exit()
    
if __name__ == "__main__":
    scope = "user-library-read playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    current_user = sp.current_user()

    playlist_name:str = input("What playlist would you like to search for? Leave empty to browse all your playlists. ")

    playlist = None
    if playlist_name == "":
        playlist = scroll_user_playlists()
    else:
        playlist = search_for_user_playlist(playlist_name)