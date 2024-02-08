import os
import tarfile
import datetime

# Prompt user to select folder to compress
folder_path = input("Enter the path of the folder to compress: ")

# Display list of available compressed file types
print("Available compressed file types:")
print("1. .zip")
print("2. .tar")
print("3. .tgz")

# Prompt user to select desired compressed file type
compress_type = input("Enter the number of the desired compressed file type: ")

# Create compressed file name
now = datetime.datetime.now()
compressed_file_name = folder_path + "_" + str(now.year) + "_" + str(now.month) + "_" + str(now.day)

# Compress folder using selected compressed file type
if compress_type == "1":
    with zipfile.ZipFile(compressed_file_name + ".zip", "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zip.write(os.path.join(root, file))
    print("Folder compressed successfully as .zip file.")
elif compress_type == "2":
    with tarfile.open(compressed_file_name + ".tar", "w") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))
    print("Folder compressed successfully as .tar file.")
elif compress_type == "3":
    with tarfile.open(compressed_file_name + ".tgz", "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))
    print("Folder compressed successfully as .tgz file.")
else:
    print("Invalid compressed file type selected.")
