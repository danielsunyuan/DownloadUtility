import subprocess
import os

class VideoDownloader:
    def __init__(self, link=None, download_dir="downloaded_videos", bash_script_path="commands.sh"):
        self.links_filepath = "video_links.txt"
        self.download_dir = download_dir
        self.bash_script_path = bash_script_path

        if link is not None:
            self.links = [link]
        else:
            self.links = []

    def links_from_file(self):
        # Read video links from the external file
        with open(self.links_filepath, "r") as file:
            self.links = file.read().splitlines()

    def bash_shell(self):
        # Open the Bash script for writing
        with open(self.bash_script_path, "w") as bash_script:
            # Write the Conda activation command to the script
            bash_script.write("#!/bin/bash\n")
            bash_script.write("source activate utility\n")

            # Ensure the output directory exists
            os.makedirs(self.download_dir, exist_ok=True)

            # Write each video link to the script and specify the download directory
            for link in self.links:
                download_command = f"yt-dlp '{link}' --recode-video mp4 -o '{self.download_dir}/%(title)s.%(ext)s'\n"
                bash_script.write(download_command)

        # Make and run the Bash script executable
        subprocess.run(["chmod", "+x", self.bash_script_path])
        subprocess.run(["./" + self.bash_script_path])

    def download_videos(self):
        # If no argument is passed into the class.. then read from the file
        if not self.links:
            self.links_from_file()
        self.bash_shell()

if __name__ == "__main__":
    # Create an instance of the VideoDownloader class
    downloader = VideoDownloader()

    # Call the download_videos method to start the video download process
    downloader.download_videos()
