import subprocess
import os

# Read YouTube links from the external file
with open("video_links.txt", "r") as file:
    video_links = file.read().splitlines()

# Create a directory for downloading videos
download_dir = "downloaded_videos"  # Replace with your desired directory name

# Path to the Bash script
bash_script_path = "commands.sh"  # Replace with the actual path

# Open the Bash script for writing
with open(bash_script_path, "w") as bash_script:
    # Write the Conda activation command to the script
    bash_script.write("#!/bin/bash\n")
    bash_script.write("source activate util_video\n")

    # Write each video link to the script and specify the download directory
    for link in video_links:
        download_command = f"yt-dlp '{link}' --recode-video mp4 -o '{download_dir}/%(title)s.%(ext)s'\n"
        bash_script.write(download_command)

# Make the Bash script executable
subprocess.run(["chmod", "+x", bash_script_path])

# Run the Bash script to download videos
subprocess.run(["./" + bash_script_path])

# Get the path to the user's Downloads directory
downloads_dir = os.path.expanduser("~/Downloads")

# Move the downloaded videos to the Downloads directory
for video_link in video_links:
    video_id = video_link.split("=")[-1]
    video_filename = f"{video_id}.mp4"
    source_path = os.path.join(download_dir, video_filename)
    destination_path = os.path.join(downloads_dir, video_filename)
    
    if os.path.exists(source_path):
        os.rename(source_path, destination_path)

# Optionally, remove the download directory if it's empty
if not os.listdir(download_dir):
    os.rmdir(download_dir)
