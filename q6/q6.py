import spotipy
import spotipy.util as util
import sys
from config import USERNAME, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI
from bs4 import BeautifulSoup as bbss
import requests
import json

scope = 'user-read-currently-playing user-modify-playback-state user-read-private playlist-modify-private playlist-modify-public playlist-read-private user-library-modify user-read-recently-played user-top-read'
token = spotipy.util.prompt_for_user_token(USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)


if token:
    sp = spotipy.Spotify(auth=token)
    current_song = sp.currently_playing()
    #print(current_song)
    artist = current_song['item']['artists'][0]['name']
    song_name = current_song['item']['name']
    print("song name is ",song_name)
    print("artist name is",artist)
    final_song = str(song_name).strip().replace(' ', '-')
    final_artist = str(artist).strip().replace(' ', '-')
    song_url = final_artist + "-" + final_song + "-" + "lyrics"
    #song_url = '{}-{}-lyrics'.format(str(artist).strip().replace(' ', '-'),str(song_name).strip().replace(' ', '-'))
    #print('\nSong: {}\nArtist: {}'.format(song_name, artist))
    #request = requests.get("https://genius.com/{}".format(song_url))
    song_final_url = "https://genius.com/" + song_url
    request = requests.get(song_final_url)
    if request.status_code == 200:
        html_code = bbss(request.text, "html.parser")
        lyrics = html_code.find("div", {"class": "lyrics"}).get_text()
        print(lyrics)

    else:
        print("Lyrics not found for current song")

    recoms = sp.recommendation_genre_seeds()
    str1 = recoms['genres'][0]
    str2 = recoms['genres'][1]
    str3 = recoms['genres'][2]
    print("Your top 3 Genres are:")
    print('1.',str1)
    print('2.',str2)
    print('3.',str3)

    topt = sp.current_user_top_tracks(20,0,'medium_term')
    topitems = topt["items"]
    count = 0
    tsongs = []
    print("Your top 20 songs on spotify are:")
    for i in topitems:
        count = count + 1
        print(count ," ",i['album']['name'])
        tsongs.append(i['album']['name'])
    print("If you want lyrics for anyone of them enter 1 else enter 2")
    cho = input()
    if(cho=="1"):
        print("Enter number of track to get lyrics (between 1-20)")
        numb = input()
        nu = int(numb)
        #print("Your entered ",numb)
        #print(topitems[nu-1]['album']['artists'][0]['name'])
        song_na = tsongs[nu-1]
        arti_na = topitems[nu-1]['album']['artists'][0]['name']
        final_song_2 = str(song_na).strip().replace(' ', '-')
        final_artist_2 = str(arti_na).strip().replace(' ', '-')
        print(final_song_2)
        print(final_artist_2)
        song_url_2 = final_artist_2 + "-" + final_song_2 + "-" + "lyrics"
        song_final_url_2 = "https://genius.com/" + song_url_2
        request_2 = requests.get(song_final_url_2)
        if request_2.status_code == 200:
            html_code = bbss(request_2.text, "html.parser")
            lyrics_2 = html_code.find("div", {"class": "lyrics"}).get_text()
            print("Here are the lyrics")
            print(lyrics_2)

        else:
            print("Lyrics not found for current song")

    #print(json.dumps(topt,indent=4, sort_keys=True))

    rec = sp.new_releases()
    #recc = json.loads(str(rec))
    #print("This is rec")
    #print(recoms)
    #print(json.dumps(rec,indent=4, sort_keys=True))

else:
    print("There was some problem with getting spotify token of ", username)
