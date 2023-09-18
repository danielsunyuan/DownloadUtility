import subprocess
import os

class LinkToAudioDownloader:
    def __init__(self, links_file, download_dir, bash_script_path):
        self.links_file = links_file
        self.download_dir = download_dir
        self.bash_script_path = bash_script_path

    def download_audio(self):
        
        # Read audio links from the external file
        with open(self.links_file, "r") as file:
            links = file.read().splitlines()

        # Open the Bash script for writing
        with open(self.bash_script_path, "w") as bash_script:
            bash_script.write("#!/bin/bash\n")
            bash_script.write("source activate utility\n")

            # Write each audio link to the script and specify the download directory
            for link in links:
                download_command = f"yt-dlp '{link}' -x --audio-format wav -o '{self.download_dir}/%(title)s.%(ext)s'\n"
                bash_script.write(download_command)

        # Make and Run the Bash script executable
        subprocess.run(["chmod", "+x", self.bash_script_path])
        subprocess.run(["./" + self.bash_script_path])
        
        # Clear the bash script
        with open(self.bash_script_path, "w"):
            pass

if __name__ == "__main__":

    downloader = LinkToAudioDownloader(
        links_file="links.txt",
        download_dir="downloaded_audio",
        bash_script_path="commands.sh"
        )
    
    downloader.download_audio()