#!/bin/bash
source activate util_video
yt-dlp 'https://www.youtube.com/watch?v=q6EoRBvdVPQ' --recode-video mp4 -o 'downloaded_videos/%(title)s.%(ext)s'
