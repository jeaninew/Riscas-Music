#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install spotipy')


# In[ ]:


import pandas as pd 
import csv
import spotipy 
sp = spotipy.Spotify() 


# In[ ]:


from spotipy.oauth2 import SpotifyClientCredentials 
cid ="your Spotify Credentials" 
secret = "your Spotify Password" 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
sp.trace=False 


# In[ ]:


# Riscas
playlist = sp.user_playlist("Riscas: The Collection", "spotify:playlist:53b4pPJq7tFktuan8LABQT") 
# uri 53b4pPJq7tFktuan8LABQT
# URL: https://open.spotify.com/playlist/53b4pPJq7tFktuan8LABQT
songs = playlist["tracks"]["items"] 
ids = []
def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        print(
            "   %d %32.32s %s" %
            (i, track['artists'][0]['name'], track['name']))
for i in range(1): 
    results = sp.playlist(playlist['id'], fields="tracks,next")
    tracks = results['tracks']
    show_tracks(tracks)
    while tracks['next']:
        tracks = sp.next(tracks)
        show_tracks(tracks)
for i in range(len(songs)): 
    ids.append(songs[i]["track"]["id"])
    features = sp.audio_features(ids)
df = pd.DataFrame(features)
print(df)


# In[ ]:


df.to_excel('Riscas.xlsx', index = False)

