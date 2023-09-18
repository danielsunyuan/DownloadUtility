import subprocess
import os

class AudioStemExtractor:
    def __init__(self, audio_directory, download_dir, bash_script_path):
        self.audio_directory = audio_directory
        self.download_dir = download_dir
        self.bash_script_path = bash_script_path

    def extract_stems(self):
        # Get the script's directories and place into variables
        script_dir = os.path.dirname(os.path.abspath(__file__))
        audio_directory = os.path.join(script_dir, self.audio_directory)

        # Open & Write the Bash script
        with open(self.bash_script_path, "w") as bash_script:
            bash_script.write("#!/bin/bash\n")
            bash_script.write(f"cd {script_dir}\n")
            bash_script.write("source activate spleeter\n")

            # Ensure the output directory exists
            os.makedirs(self.download_dir, exist_ok=True)

            # Iterate over audio files in the directory
            for audio_file in os.listdir(audio_directory):
                # Check if the file is a valid audio file (e.g., with a .mp3 or .wav extension)
                if audio_file.endswith(".mp3") or audio_file.endswith(".wav"):
                    audio_path = os.path.join(audio_directory, audio_file)

                    # Use spleeter to separate the audio
                    download_command = f"spleeter separate -p spleeter:2stems-16kHz -o {self.download_dir} '{audio_path}'\n"
                    bash_script.write(download_command)

        # Make and run the Bash script executable
        subprocess.run(["chmod", "+x", self.bash_script_path])
        subprocess.run(["./" + self.bash_script_path])

if __name__ == "__main__":
    # Create an instance of the AudioStemExtractor class
    extractor = AudioStemExtractor(
        audio_directory="audio",
        download_dir="audio_stems",
        bash_script_path="commands.sh"
    )

    # Call the extract_stems method to start the extraction process
    extractor.extract_stems()