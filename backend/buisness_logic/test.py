import unittest

from buisness_logic.SpotifyWebAPI.features import Spotify
from buisness_logic.rocknationAPI import get_link_on_artist, get_link_on_track, get_artist_name, get_album_name, \
    get_album_release_year
from buisness_logic.spotifyPythonAPI import get_artists_ids_and_names, get_top_music_info, \
    get_top_music_info_by_approximate_artist_title

token = 'BQCN2-Nf9aK1HqnGyQT30vp9ikMjGyOFpGs9z60PsGltKpa65JdEu2H83bVtgNW83xHxpSblI4IzR2Ai-OTOzAR90mHyx9dSKHpy2hMtG5ym508jdivmWDFCQHcPCMlkbl-2dqVQcayYbPDfy3M7swRLr5FV2AKPidhaD3EVBAKqJTcV8F2CRPWFegZwqOiZkFfLFZDu1ZRz_TbdWFSmpO57-sIPChrYyxSm5K1TvWiqkqdNqS3Fh3dO6TGsTpXuKoCv9rn5eSuEreKLPGReHo34Urx-C5rk'
ac_dc_spotify_id = '711MCceyCBcFnzjGY4Q7Un'

artist_name = 'AC/DC'
album_name = 'back in black'
track_name = 'back in black'
release_year = '1980'

spotify = Spotify()


class SpotifyAPITestCases(unittest.TestCase):
    def testGetArtistsIdsAndNames(self):
        artists_ids_and_names = get_artists_ids_and_names('ac dc', spotify=spotify)

        self.assertEqual(len(artists_ids_and_names), 1)
        self.assertEqual(artists_ids_and_names[0]['artist_title'], 'AC/DC')
        self.assertEqual(artists_ids_and_names[0]['artist_id'], ac_dc_spotify_id)

    def testGetTopMusicInfo(self):
        top_music_info = get_top_music_info(ac_dc_spotify_id, spotify)

        self.assertEqual(len(top_music_info), 10)

    def testGetTopMusicInfoByApproximateArtistTitle(self):
        top_music_info = get_top_music_info_by_approximate_artist_title(artist_name, spotify=spotify)

        self.assertEqual(len(top_music_info), 10)


class DownloadTracksTestCase(unittest.TestCase):
    def testGetLinkOnArtist(self):
        link = get_link_on_artist(artist_name)

        self.assertNotEqual(link, None)

    def testGetLinkOnTrack(self):
        link = get_link_on_track(approximate_artist_name=artist_name, approximate_track_name=track_name,
                                 approximate_album_name=album_name)

        self.assertEqual(link,
                         "https://rocknation.su/upload/mp3/AC-DC/1980%20-%20Back%20In%20Black/"
                         "06.%20Back%20In%20Black.mp3")

    def testGetArtistName(self):
        artist_name = 'kiss'
        rock_name = get_artist_name(artist_name)
        self.assertEqual(rock_name, 'Kiss')

    def testGetAlbumName(self):
        rock_name = get_album_name(approximate_artist_name=artist_name, approximate_album_name=album_name)
        self.assertEqual(rock_name, 'Back in Black')

    def testGetAlbumReleaseDate(self):
        rock_name = get_album_release_year(approximate_artist_name=artist_name, approximate_album_name=album_name)
        self.assertEqual(rock_name, release_year)


if __name__ == '__main__':
    unittest.main()
