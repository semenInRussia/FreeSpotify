from django.shortcuts import render

# Create your views here.
from django.views import View

from buisness_logic.SpotifyWebAPI.features import Spotify
from buisness_logic.spotifyPythonAPI import get_top_music_info_by_approximate_artist_title

from backend.buisness_logic.publicFeatures import get_tracks_top

spotify = Spotify()


class TopView(View):
    template = "top.html"

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        artist_name = request.POST.get("artist_name")

        try:
            tracks_info = get_tracks_top(artist_name, spotify=spotify)
        except TypeError:
            return render(request, self.template)
        else:
            return render(request, self.template, context={
                "tracks_info": tracks_info
            })
