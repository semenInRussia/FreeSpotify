from backend.buisness_logic.SpotifyWebAPI.features import Spotify
from backend.buisness_logic.rocknationAPI import get_link_on_album, get_link_on_artist
from backend.buisness_logic.spotifyPythonAPI import get_top_music_info, get_top_music_info_by_approximate_artist_title


def get_tracks_top(artist_name, spotify: Spotify) -> list:
    tracks_info = get_top_music_info_by_approximate_artist_title(artist_name, spotify=spotify)

    tracks_info__out = []
    for spotify_track_info in tracks_info:
        artist_name = spotify_track_info["artist_name"]
        album_name = spotify_track_info["album_name"]

        spotify_track_info["album_link"] = get_link_on_album(artist_name, album_name)
        spotify_track_info["artist_link"] = get_link_on_artist(artist_name)
        tracks_info__out.append(spotify_track_info)

    return tracks_info__out
