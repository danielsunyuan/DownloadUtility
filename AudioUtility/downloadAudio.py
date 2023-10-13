import subprocess

class LinkToAudioDownloader:
    def __init__(self, download_dir, bash_script_path, link=None):
        self.links_file = "audio_links.txt"
        self.download_dir = download_dir
        self.bash_script_path = bash_script_path
        
        if link is not None:
            self.links = [link]
        else:
            self.links = []

    def links_from_file(self):
        # Read audio links from the external file
        with open(self.links_file, "r") as file:
            self.links = file.read().splitlines()

    def bash_shell(self):
        # Open the Bash script for writing
        with open(self.bash_script_path, "w") as bash_script:
            bash_script.write("#!/bin/bash\n")
            bash_script.write("source activate utility\n")

            # Write each audio link to the script and specify the download directory
            for link in self.links:
                download_command = f"yt-dlp '{link}' -x --audio-format wav -o '{self.download_dir}/%(title)s.%(ext)s'\n"
                bash_script.write(download_command)

        # Make and Run the Bash script executable
        subprocess.run(["chmod", "+x", self.bash_script_path])
        subprocess.run(["./" + self.bash_script_path])

        # Clear the bash script
        with open(self.bash_script_path, "w"):
            pass

    def download_audio(self):
        # If no argument is passed into the class.. then read from the file
        if not self.links:
            self.links_from_file()
        self.bash_shell()

if __name__ == "__main__":
    downloader = LinkToAudioDownloader(
        # Flume - 71m3
        link="https://www.youtube.com/watch?v=9DJS_aNGxHI",
        download_dir="downloaded_audio",
        bash_script_path="commands.sh"
    )
    
    downloader.download_audio()
