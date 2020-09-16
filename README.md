# spotify_playlist_manager

This script transfers every song saved in a public Youtube Playlist into a Spotify Playlist

Requirements for this to work:
- A Spotify Developper Account, which is not difficult to set up
(https://developer.spotify.com/)

- All the Python Libraries installed, that are imported on the top of app.py

- Every variable in secret.py has to have a value. (There are some Comments in the code that help)

How it works:

- The script first gets all the video titles of your public Youtube Playlist by Webscraping(no selenium needed)

- Next it searches for these Songs on Spotify

- Every song, that Spotify finds will be added to the Spotify Playlist

Best use:

- By running the script the Playlist will only update once. You can just deploy the script on a server that runs it every minute or whatever you like. 