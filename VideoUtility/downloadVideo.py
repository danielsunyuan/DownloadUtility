import subprocess
import os

class VideoDownloader:
    def __init__(self, links_file="video_links.txt", download_dir="downloaded_videos", bash_script_path="commands.sh"):
        self.links_file = links_file
        self.download_dir = download_dir
        self.bash_script_path = bash_script_path

    def download_videos(self):
        # Read video links from the external file
        with open(self.links_file, "r") as file:
            video_links = file.read().splitlines()

        # Open the Bash script for writing
        with open(self.bash_script_path, "w") as bash_script:
            # Write the Conda activation command to the script
            bash_script.write("#!/bin/bash\n")
            bash_script.write("source activate utility\n")

            # Ensure the output directory exists
            os.makedirs(self.download_dir, exist_ok=True)

            # Write each video link to the script and specify the download directory
            for link in video_links:
                download_command = f"yt-dlp '{link}' --recode-video mp4 -o '{self.download_dir}/%(title)s.%(ext)s'\n"
                bash_script.write(download_command)

        # Make and run the Bash script executable
        subprocess.run(["chmod", "+x", self.bash_script_path])
        subprocess.run(["./" + self.bash_script_path])

if __name__ == "__main__":
    # Create an instance of the VideoDownloader class
    downloader = VideoDownloader()

    # Call the download_videos method to start the video download process
    downloader.download_videos()
