import subprocess
import os

class AudioStemExtractor:
    def __init__(self, audio_directory, download_dir, bash_script_path, stem_number):
        self.audio_directory = audio_directory
        self.download_dir = download_dir
        self.bash_script_path = bash_script_path
        self.stem_number = stem_number

    def extract_stems(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        audio_directory = os.path.join(script_dir, self.audio_directory)

        with open(self.bash_script_path, "w") as bash_script:
            bash_script.write("#!/bin/bash\n")
            bash_script.write(f"cd {script_dir}\n")
            bash_script.write("source activate spleeter\n")

            # Ensure the output directory exists
            os.makedirs(self.download_dir, exist_ok=True)

            for audio_file in os.listdir(audio_directory):
                if audio_file.endswith(".mp3") or audio_file.endswith(".wav"):
                    audio_path = os.path.join(audio_directory, audio_file)

                    download_command = f"spleeter separate -p spleeter:{self.stem_number}stems-16kHz -o {self.download_dir} '{audio_path}'\n"
                    bash_script.write(download_command)

        # Make and run the Bash script executable
        subprocess.run(["chmod", "+x", self.bash_script_path])
        subprocess.run(["./" + self.bash_script_path])

        # Clear the bash script
        with open(self.bash_script_path, "w"):
            pass

    def clear_download_directory(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        audio_directory = os.path.join(script_dir, self.audio_directory)
        
        for audio_file in os.listdir(audio_directory):
            audio_path = os.path.join(audio_directory, audio_file)
            if os.path.isfile(audio_path):
                os.remove(audio_path)


if __name__ == "__main__":

    splitter = AudioStemExtractor(
        audio_directory="audio",
        download_dir="output",
        bash_script_path="commands.sh"
    )

    splitter.extract_stems()
    splitter.clear_download_directory()