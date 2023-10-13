#!/bin/bash
source activate utility
yt-dlp 'https://www.youtube.com/watch?v=UVtTc4zqbxQ' --recode-video mp4 -o '/Users/duan/Downloads/%(title)s.%(ext)s'
