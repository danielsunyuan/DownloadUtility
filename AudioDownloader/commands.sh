#!/bin/bash
source activate utility
yt-dlp 'https://www.youtube.com/watch?v=q6EoRBvdVPQ' -x --audio-format wav -o 'downloaded_audio/%(title)s.%(ext)s'
