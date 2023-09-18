import os
from AudioUtility.downloadAudio import LinkToAudioDownloader
from Splitter.split import AudioStemExtractor

def main():
    # Create an instance of the LinkToAudioDownloader class
    audio_downloader = LinkToAudioDownloader(
        links_file="links.txt",
        download_dir="Splitter/audio",
        bash_script_path="AudioUtility/commands.sh"
    )

    # Call the download_audio method to download audio files
    audio_downloader.download_audio()

    # Define the audio directories
    audio_splitter_dir = "Splitter/audio_stems"
    output_dir = f"{os.path.dirname(os.path.abspath(__file__))}/Output"

    # Create an instance of the AudioStemExtractor class
    audio_splitter = AudioStemExtractor(
        audio_directory="audio",
        download_dir=output_dir,
        bash_script_path="Splitter/commands.sh"
    )
    # Call the extract_stems method to extract audio stems
    audio_splitter.extract_stems()

    # Move extracted audio stems back to the root directory
    for stem_file in os.listdir(audio_splitter_dir):
        stem_path = os.path.join(audio_splitter_dir, stem_file)
        if os.path.isfile(stem_path):
            new_path = os.path.join(os.getcwd(), stem_file)
            os.rename(stem_path, new_path)

if __name__ == "__main__":
    main()