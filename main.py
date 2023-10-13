import os
import shutil
import argparse
from AudioUtility.downloadAudio import LinkToAudioDownloader
from Splitter.split import AudioStemExtractor
from VideoUtility.downloadVideo import VideoDownloader

def main():

    # Arguments
    parser = argparse.ArgumentParser(description="Download and process audio from a link.",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("link",
                        help="link to download audio from")
    
    parser.add_argument("-v", "--video",
                        action="store_true",
                        dest="video",
                        help="Download Video",
                        )

    parser.add_argument("-a", "--audio",
                        action="store_true",
                        dest="audio",
                        help="Download Audio",
                        )
    
    parser.add_argument("-s", "--stems",
                        action="store_true",
                        dest="stems",
                        help="Extract Stems from Link",
                        )

    parser.add_argument("-acca", "--accapella",
                        action="store_true",
                        dest="accapella",
                        help="Extract Accapella from Link",
                        )

    parser.add_argument("-inst", "--instrumental",
                        action="store_true",
                        dest="instrumental",
                        help="Extract Instrumental from Link",
                        )

    parser.add_argument("-o", "--output-dir",
                        dest="output_dir",
                        help="Output directory to store downloaded or processed files"
    )

    options = parser.parse_args()


    # Determine the output directory
    if options.output_dir:
        output_dir = options.output_dir
    else:
        user_home = os.path.expanduser("~")
        output_dir = os.path.join(user_home, "Downloads")


    links = options.link.split(",")  # Split multiple links by a comma
    links = options.link


    if options.audio:
        audio_downloader(links, output_dir)

    if options.video:
        video_downloader(links, output_dir)

    if options.stems:
        stem_download(links, output_dir, stem_num=4)

    if options.accapella:
        stem_download(links, output_dir, stem_num=2)
        raise NotImplementedError

    if options.instrumental:
        stem_download(links, output_dir, stem_num=2)
        raise NotImplementedError

    print(f"Files ready ---> {output_dir}")


def audio_downloader(links, output_dir):
    # Download audio from the provided link
    audio_downloader = LinkToAudioDownloader(
        link=links,
        download_dir=output_dir,
        bash_script_path="commands.sh"
    )

    audio_downloader.download_audio()

    return

def video_downloader(links, output_dir):
    video_downloader = VideoDownloader(
        link=links,
        download_dir=output_dir
    )

    video_downloader.download_videos()

    return

def stem_download(links, output_dir, stem_num):
    # Download audio from the provided link

    audio_downloader = LinkToAudioDownloader(
        link=links,
        download_dir="Splitter/__audio__",
        bash_script_path="AudioUtility/commands.sh"
    )
    splitter = AudioStemExtractor(
        audio_directory="__audio__",
        download_dir="__processing__",
        bash_script_path="Splitter/commands.sh",
        stem_number=str(stem_num)
    )

    splitter.clear_download_directory()
    audio_downloader.download_audio()
    splitter.extract_stems()

    return

if __name__ == "__main__":
    main()