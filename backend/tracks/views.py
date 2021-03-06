from django.http import JsonResponse

# Create your views here.
from buisness_logic.SpotifyWebAPI.features import Spotify
from buisness_logic.spotifyPythonAPI import get_track_info, get_tracks_info, \
    get_top_music_info_by_approximate_artist_title

from buisness_logic.publicFeatures import get_tracks_top

spotify = Spotify()

def get_track_view(request, artist, album, track):
    data = get_track_info(artist_name=artist, track_name=track, spotify=spotify)

    assert data is not None

    return JsonResponse(data, safe=False)


def view_tracks_info(request, artist):
    data = get_tracks_top(artist, spotify=spotify)

    assert data is not None

    return JsonResponse(data, safe=False)
