from backend.buisness_logic.SpotifyWebAPI.features import Spotify
from backend.buisness_logic.core.exceptions import NotFoundAlbumException, NotFoundArtistException
from backend.buisness_logic.rocknationAPI import get_link_on_album, get_link_on_artist
from backend.buisness_logic.spotifyPythonAPI import get_top_music_info, get_top_music_info_by_approximate_artist_title


def get_tracks_top(artist_name, spotify: Spotify) -> list:
    tracks_info = get_top_music_info_by_approximate_artist_title(artist_name, spotify=spotify)

    cash = {
        'links_on_album': {},
    }

    link_on_artist = ""

    for track in tracks_info:

        artist_name = track["artist_name"]
        album_name = track['album_name']

        # get link on artist
        if link_on_artist == "":
            link_on_artist = get_link_on_artist(artist_name)

        # get link on album
        link_on_album = cash['links_on_album'].get(album_name)
        if not link_on_album:
            link_on_album = get_link_on_album(artist_name, album_name, raise_exception=False)
            cash['links_on_album'][album_name] = link_on_album

        # update data
        track["album_link"] = link_on_album
        track["artist_link"] = link_on_artist

    return tracks_info
