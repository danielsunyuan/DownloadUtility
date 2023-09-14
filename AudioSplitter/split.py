import subprocess
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path to your audio directory within the parent directory
audio_directory = os.path.join(script_dir, "audio")

# Create a directory for downloading audio stems
download_dir = "audio_stems"

# Path to the Bash script
bash_script_path = "commands.sh"

# Open the Bash script for writing
with open(bash_script_path, "w") as bash_script:
    # Write the Conda activation command to the script
    bash_script.write("#!/bin/bash\n")
    bash_script.write("source activate spleeter\n")

    # Ensure the output directory exists
    os.makedirs(download_dir, exist_ok=True)

    # Iterate over audio files in the directory
    for audio_file in os.listdir(audio_directory):
        # Check if the file is a valid audio file (e.g., with a .mp3 or .wav extension)
        if audio_file.endswith(".mp3") or audio_file.endswith(".wav"):
            audio_path = os.path.join(audio_directory, audio_file)
            
            # Use spleeter to separate the audio
            download_command = f"spleeter separate -p spleeter:2stems -o {download_dir} '{audio_path}'\n"
            bash_script.write(download_command)

# Make the Bash script executable
subprocess.run(["chmod", "+x", bash_script_path])

# Run the Bash script to separate audio
subprocess.run(["./" + bash_script_path])
