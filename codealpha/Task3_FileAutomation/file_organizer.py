import os
import shutil

# Get the folder where this Python file is located
base_folder = os.path.dirname(os.path.abspath(__file__))

source_folder = os.path.join(base_folder, "source")
destination_folder = os.path.join(base_folder, "destination")

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Find and move JPG/JPEG files
for file in os.listdir(source_folder):

    if file.lower().endswith((".jpg", ".jpeg")):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print("Moved:", file)

print("\nAll image files moved successfully!")