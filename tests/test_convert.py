from unittest import TestCase, main

from youtube_to_osu import convert

import os


class TestConvert(TestCase):
    @classmethod
    def teardown_class(cls):
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
            last_timestamp_seen = int(sections[2])
            assert len(sections) == 6, "Checking proper sections"
            assert int(sections[0]) in [64, 192, 320, 448], "1st section"
            assert int(sections[1]) in 192, "2nd section check"
            assert int(sections[2]) >= last_timestamp_seen, "Timestamp is increasing"
            assert int(sections[3]), 1
            assert int(sections[4]), 0
            assert str(sections[5]) == "0:0:0:0:"


if __name__ == "__main__":
    main()
