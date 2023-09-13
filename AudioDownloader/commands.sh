#!/bin/bash
source activate util_video
yt-dlp 'https://www.youtube.com/playlist?list=PLkWGJ-Z0Er_KLNz6eBB-D-R6kR2T1Pfnd' -x --audio-format wav -o 'downloaded_audio/%(title)s.%(ext)s'
