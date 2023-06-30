# Import the necessary modules
import os
import shutil

# Define the source directory containing the files to be organized
# Taking raw input which won't interpret escape characters
source_dir = input(r"Enter the source directory path : ").replace('\\', '/')

# Define the destination directory where the organized files will be moved to
# Taking raw input which won't interpret escape characters
dest_dir = input(r"Enter the destination directory path : ").replace('\\', '/')

# Create a dictionary to map file extensions to their respective folders
extension_map = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.jpeg': 'Images',
    'TIFF' : 'Images',
    '.webp' : 'Images',
    '.avif' : 'Images',
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Documents',
    '.rtf' : 'Documents',
    '.pptx': 'Documents',
    '.ppt': 'Documents',
    '.mp3': 'Audio',
    '.wav': 'Audio',
    '.mp4': 'Video',
    '.avi': 'Video',
    '.exe': 'Apps',
    '.zip': 'Zip_Files'
}

# Create the destination folders if they don't already exist
for folder_name in set(extension_map.values()):
    os.makedirs(os.path.join(dest_dir, folder_name), exist_ok=True)

# Loop through each file in the source directory and move it to the appropriate folder in the destination directory
for filename in os.listdir(source_dir):
    file_ext = os.path.splitext(filename)[-1].lower()  # get the file extension in lowercase
    if file_ext in extension_map:  # check if the file extension is in the extension_map dictionary
        src_path = os.path.join(source_dir, filename)  # create the full path to the source file
        dest_path = os.path.join(dest_dir, extension_map[file_ext], filename)  # create the full path to the destination file
        shutil.move(src_path, dest_path)  # move the file to the appropriate folder in the destination directory