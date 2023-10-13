import os
import argparse
from AudioUtility.downloadAudio import LinkToAudioDownloader
from Splitter.split import AudioStemExtractor
from VideoUtility.downloadVideo import VideoDownloader

def main():

    # Arguments
    parser = argparse.ArgumentParser(description="Download and process audio from a link.",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("link", \
                        help="link to download audio from")
    
    parser.add_argument("-v", "--video", \
                        action="store_true", \
                        dest="video_link", \
                        help="Required: Valid Link to Video", \
                        )

    parser.add_argument("-a", "--audio", \
                        action="store_true", \
                        dest="audio_link", \
                        help="Required: Valid Link to Video", \
                        )
    
    parser.add_argument("-s", "--stems", \
                        action="store_true", \
                        dest="stems_link", \
                        help="Required: Valid Link to Video", \
                        )

    parser.add_argument("-acca", "--accapella", \
                        action="store_true", \
                        dest="accapella_link", \
                        help="Required: Valid Link to Video", \
                        )

    parser.add_argument("-inst", "--instrumental", \
                        action="store_true", \
                        dest="instrumental_link", \
                        help="Required: Valid Link to Video", \
                        )


    options = parser.parse_args()
    links = options.link.split(",")  # Split multiple links by a comma
    links = options.link

    # Output directory
    user_home = os.path.expanduser("~")
    output_dir = os.path.join(user_home, "Downloads")

    if options.audio_link:
        audio_downloader(links, output_dir)

    if options.video_link:
        video_downloader(links, output_dir)

    if options.stems_link:
        stems_download(links, output_dir)

    print(f"Files ready ---> {output_dir}")


def audio_downloader(links, output_dir):
    # Download audio from the provided link
    audio_downloader = LinkToAudioDownloader(
        link=links,
        download_dir=output_dir,
        bash_script_path="AudioUtility/commands.sh"
    )

    audio_downloader.download_audio()

    return

def video_downloader(links, output_dir):
    video_downloader = VideoDownloader(
        link=links,
        download_dir=output_dir
    )

    video_downloader.download_videos()


def stems_download(links, output_dir):
    # Download audio from the provided link

    audio_downloader = LinkToAudioDownloader(
        link=links,
        download_dir="Splitter/__audio__",
        bash_script_path="AudioUtility/commands.sh"
    )
    splitter = AudioStemExtractor(
        audio_directory="__audio__",
        download_dir=output_dir,
        bash_script_path="Splitter/commands.sh"
    )

    splitter.clear_download_directory()
    audio_downloader.download_audio()
    splitter.extract_stems()

    return



if __name__ == "__main__":
    main()