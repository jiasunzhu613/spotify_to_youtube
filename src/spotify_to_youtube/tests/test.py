import unittest
from spotify_to_youtube.spotify import calculate_title_similarity, is_song_in_playlist
import sys
from pathlib import Path

# Note: when running with dependencies with files from parent directories, make sure to run 
# python3 -m spotify_to_youtube.tests.test
class TestSpotify(unittest.TestCase):
    def Test_Calculate_Title_Similarity(self):
        QUARTILE3 = 0.75
        self.assertGreater(calculate_title_similarity("【MV】Creepy Nuts - 二度寝(Nidone)", "二度寝 - nidone", "creepy nuts"), QUARTILE3)
        self.assertGreater(calculate_title_similarity("ZUTOMAYO - Truth In Lies (Music Video)", "二度寝 - nidone", "creepy nuts"), QUARTILE3)
        self.assertGreater(calculate_title_similarity("SawanoHiroyuki[nZk]:Laco「FAKEit」Music Video Fate/strange Fake -Whispers of Dawn- ver.", "二度寝 - nidone", "creepy nuts"), QUARTILE3)
        self.assertGreater(calculate_title_similarity("SennaRin「melt」Music Video('Legend of the Galactic Heroes Die Neue These Gekitotsu' theme song)", "二度寝 - nidone", "creepy nuts"), QUARTILE3)


    def Test_Is_Song_In_Playlist(self):
        pass


if __name__ == "__main__":
    print(str(Path(__file__).parent.parent))
    unittest.main()