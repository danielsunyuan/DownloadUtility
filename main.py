import os
import argparse
from AudioUtility.downloadAudio import LinkToAudioDownloader
from Splitter.split import AudioStemExtractor

def main():

    # Arguments
    parser = argparse.ArgumentParser(description="Download and process audio from a link.")
    parser.add_argument("link", \
                        help="link to download audio from")
    
    parser.add_argument("-v", "--video", \
                        description="Download link to Video", \
                        help="Required: Valid Link to Video", \
                        type=str)

    parser.add_argument("-a", "--audio", \
                        description="Donwnload link to Audio", \
                        help="Required: Valid Link to Video", \
                        type=str)
    
    parser.add_argument("-s", "--stems", \
                        description="Extract stems from link", \
                        help="Required: Valid Link to Video", \
                        type=str)

    parser.add_argument("-acca", "--accapella", \
                        description="Extract accapella from link", \
                        help="Required: Valid Link to Video", \
                        type=str)

    parser.add_argument("-intr", "--instrumental", \
                        description="Extract instrumental from link", \
                        help="Required: Valid Link to Video", \
                        type=str)


    args = parser.parse_args()
    links = args.link

    # Output directory
    user_home = os.path.expanduser("~")
    output_dir = os.path.join(user_home, "Downloads")

    # Download audio from the provided YouTube link
    audio_downloader = LinkToAudioDownloader(
        link=links,
        download_dir="Splitter/audio",
        bash_script_path="AudioUtility/commands.sh"
    )

    splitter = AudioStemExtractor(
        audio_directory="audio",
        download_dir=output_dir,
        bash_script_path="Splitter/commands.sh"
    )

    splitter.clear_download_directory()
    audio_downloader.download_audio()
    splitter.extract_stems()

    print(f"Files ready ---> {output_dir}")

if __name__ == "__main__":
    main()
