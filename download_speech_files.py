import os
import requests

# Function to download file
def download_file(url, folder, filename):
    local_filename = os.path.join(folder, filename)
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return local_filename

# Create a folder to save the downloaded files if it doesn't exist
download_folder = 'downloads'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Get the list of files in the output folder
output_folder = "output"
files = os.listdir(output_folder)
files = [os.path.splitext(file)[0] for file in files if os.path.isfile(os.path.join(output_folder, file))]

# Read hrefs from download_urls.txt
with open("download_urls.txt", "r") as lines:
    hrefs = lines.readlines()

# Remove trailing newline characters
hrefs = [href.strip() for href in hrefs]

# Download each file
for href, filename in zip(hrefs, files):
    if href.endswith('.mp3'):
        filename = download_file(href, download_folder, filename + '.mp3')
        print("Downloaded:", filename)
