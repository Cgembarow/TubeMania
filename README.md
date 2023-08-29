# TubeMania

This is a Python module that has a helpful function for converting YouTube links into playable OSU beatmaps

```console
sudo apt update && sudo apt upgrade
sudo apt install ffmpeg
virtualenv env
source env/bin/activate
pip install -e .
```

... then test with Python interpreter

```
Python 3.10.8 (main, Aug 19 2023, 00:31:12) [GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from youtube_to_osu import convert
>>> convert("https://www.youtube.com/watch?v=9bZkp7q19f0")
Number of notes: 1127
Song length (seconds): 252.3544671201814
Average NPS: 4.465940361036989
>>>
```

## Testing

To run the included test,

```
pytest
```
