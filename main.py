import os
from AudioUtility.downloadAudio import LinkToAudioDownloader
from Splitter.split import AudioStemExtractor

def main():

    #output_dir = f"{os.path.dirname(os.path.abspath(__file__))}/output"
    user_home = os.path.expanduser("~")
    output_dir = os.path.join(user_home, "Downloads")

    audio_downloader = LinkToAudioDownloader(
        links_file="links.txt",
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