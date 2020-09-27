import requests
import numpy as np
import importlib
import re

secret = importlib.import_module("secret")


class Spotify:

    def __init__(self):
        url = "https://accounts.spotify.com/api/token"

        request_body = {"grant_type": "refresh_token", "refresh_token": secret.spotify_refresh_token}

        header = {
            "Authorization": secret.basic_authotization}

        response = requests.post(
            url,
            headers=header,
            data=request_body
        )
        self.token = response.json()["access_token"]

    def add_to_playlist(self, playlist_id, track_ids):

        if len(track_ids) != 0:
            url = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks?".format(playlist_id=playlist_id)

            request_body = {
                "uris": track_ids,
                "position": 0
            }

            header_field = {"Content-Type": "application/json",
                            "Authorization": "Bearer {token}".format(token=self.token)}

            response = requests.post(
                url=url,
                json=request_body,
                headers=header_field,

            )

            response_json = response.json()
            print(response_json)

    def get_ids_by_name(self, track_names):

        track_array = []
        for track_name in track_names:
            url = "	https://api.spotify.com/v1/search"

            header_field = {"Authorization": "Bearer {token}".format(token=self.token)}

            response = requests.get(
                url=url,
                headers=header_field,
                params={"q": "{name}".format(name=track_name),
                        "type": "track",
                        "limit": "1"}
            )

            response_json = response.json()

            if response_json["tracks"]["total"] != 0:

                track_array.append(response_json["tracks"]["items"][0]["uri"])


        return track_array

    def get_ids_in_playlist(self, playlist_id):

        track_ids = []

        url = "https://api.spotify.com/v1/playlists/{playlist_id}/tracks".format(playlist_id=playlist_id)

        header_field = {"Authorization": "Bearer {token}".format(token=self.token)}

        response = requests.get(
            url=url,
            headers=header_field,
            params={}
        )

        response_json = response.json()

        items_array = response_json["items"]  # array

        for i in items_array:
            track_ids.append(i["track"]["uri"])

        return track_ids

    def get_new_track_ids(self, playlist_id, track_ids):
        array1 = np.array(track_ids)
        array2 = self.get_ids_in_playlist(playlist_id)

        return_array = []

        for t in np.setdiff1d(array1, array2):
            return_array.append(t)
            print("neuer Song: " + t)

        return return_array





def get_tracks_yt(url):

    string_array = []

    r = requests.get(url)

    code = r.text
    print(code)
    titles = re.findall("title\":{\"runs\":\[{\"text\":\"(.*?)\"}],", code)
    #
    print(titles)
    for i in titles:
        string_array.append(i)

    return_array = []

    for t in string_array:
        t = t.lower()
        t = t.replace("official", "")
        t = t.replace("explicit", "")
        t = t.replace("version", "")
        t = t.replace("video", "")
        t = t.replace("music", "")
        t = t.replace("vevo", "")
        t = t.replace("clip", "")
        t = t.replace("officiel", "")
        t = t.replace("audio", "")
        t = t.replace("(", "")
        t = t.replace(")", "")
        t = t.replace("[", "")
        t = t.replace("]", "")
        t = t.replace("|", "")
        t = t.replace("-", "")
        t = t.replace("  ", " ")
        t = t.replace("   ", " ")
        t = t.split(" ft", 1)[0]
        t = t.split("feat", 1)[0]

        #By filtering all these Substrings the Chance of finding THe Song in Spotify increases

        return_array.append(t)

    return return_array


def update_playlist():
    yt_tracks = get_tracks_yt(secret.youtube_playlist_url)
    print("yt tracks")
    print(yt_tracks)

    sp = Spotify()
    yt_track_ids = sp.get_ids_by_name(yt_tracks)
    print(yt_track_ids)
    new_track_ids = sp.get_new_track_ids(secret.spotify_playlist_id, yt_track_ids)
    print(new_track_ids)
    sp.add_to_playlist(secret.spotify_playlist_id, new_track_ids)



update_playlist()
