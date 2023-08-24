from unittest import TestCase, main

from youtube_to_osu import convert

import os


class TestConvert(TestCase):
    @classmethod
    def tearDownClass(cls):
        os.remove("beatmap.txt")
        os.remove("beatmap.mp3")

    def test_convert(self):
        convert("https://www.youtube.com/watch?v=9bZkp7q19f0")
        self.assertTrue(os.path.exists("beatmap.txt"), "Checking file was created")

        with open("beatmap.txt") as file:
            lines = file.read().splitlines()

        last_timestamp_seen = 0
        for line in lines:
            sections = line.split(",")
            self.assertTrue(len(sections) == 6, "Checking proper sections")
            self.assertIn(
                int(sections[0]), [64, 192, 320, 448], "Checking correct channel"
            )
            self.assertIs(
                int(sections[1]), 192, "Checking 2nd section is set correctly"
            )
            self.assertGreaterEqual(int(sections[2]), last_timestamp_seen)
            last_timestamp_seen = int(sections[2])
            self.assertIs(int(sections[3]), 1)
            self.assertIs(int(sections[4]), 0)
            self.assertTrue(str(sections[5]) == "0:0:0:0:")


if __name__ == "__main__":
    main()
