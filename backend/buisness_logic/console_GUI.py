import buisness_logic
from buisness_logic.SpotifyWebAPI.features import Spotify
from buisness_logic.core.exceptions import NotFoundAlbumException
from buisness_logic.rocknationAPI import get_link_on_artist, get_link_on_track, get_link_on_album
from buisness_logic.spotifyPythonAPI import get_top_music_info_by_approximate_artist_title, get_artist_info

spotify = Spotify()


def main():
    while True:
        print("Enter group's name:")
        artist_name = input()
        try:
            print(get_link_on_artist(artist_name))
        except buisness_logic.core.exceptions.NotFoundArtistException:
            print("X3".center(30, '-'))
            print("Maybe, you think about:")
            print(f"\t{get_artist_info(artist_name, spotify=spotify)['artist_title']}")
            continue

        top = get_top_music_info_by_approximate_artist_title(artist_name, spotify)
        print_top(top)

        print("*" * 80)


def print_top(top: list):
    cash = {
        'links_on_album': {}
    }
    for track in top:
        artist_name = track['artist_name']
        name = track['name']
        album_name = track['album_name']

        print(track['top_number'])

        link_on_album = cash['links_on_album'].get(album_name)
        if not link_on_album:
            try:
                link_on_album = get_link_on_album(artist_name, album_name)
            except NotFoundAlbumException:
                link_on_album = None
            cash['links_on_album'][album_name] = link_on_album

        print(
            f'\t{album_name} {track["release_date"]} {link_on_album}'
        )

        print(f'\t\t{name}', get_link_on_track(artist_name, name, album_name))


if __name__ == "__main__":
    main()
