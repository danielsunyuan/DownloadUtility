#!/bin/bash
source activate spleeter
spleeter separate -p spleeter:2stems -o audio_stems '/Users/duan/Movies/Utility/AudioSplitter/audio/audio_example.mp3'
