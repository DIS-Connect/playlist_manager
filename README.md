# spotify_playlist_manager

This script transfers every song saved in a public Youtube Playlist into a Spotify Playlist

Requirements for this to work:
- A Spotify Developper Account, which is not difficult to set up
(https://developer.spotify.com/)

- All the Python Libraries installed, that are imported on the top of app.py

- Every variable in secret.py has to have a value.(some help for the refresh_token)

How it works:

- The script first gets all the video titles of your public Youtube Playlist

- Next it searches for these Songs on Spotify

- If it finds a song, it adds it to your spotify playlist