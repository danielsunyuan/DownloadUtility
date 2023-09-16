#!/bin/bash
source activate utility
yt-dlp 'https://www.youtube.com/watch?v=I4DjHHVHWAE' -x --audio-format wav -o 'Splitter/audio/%(title)s.%(ext)s'
