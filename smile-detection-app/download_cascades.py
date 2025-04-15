import urllib.request
import os

def download_file(url, filename):
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded {filename} successfully!")

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# URLs for the Haar Cascade files
face_cascade_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
smile_cascade_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_smile.xml"

# Download the files
download_file(face_cascade_url, os.path.join(current_dir, 'haarcascade_frontalface_default.xml'))
download_file(smile_cascade_url, os.path.join(current_dir, 'haarcascade_smile.xml'))

print("All files downloaded successfully!") 