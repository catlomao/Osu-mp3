import os
import shutil

def copy_and_rename_mp3_files(input_dir, output_dir):
    count = 1
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower() == 'audio.mp3':
                source_path = os.path.join(root, file)
                destination_path = os.path.join(output_dir, f"{count}.mp3")
                shutil.copy2(source_path, destination_path)
                print(f"Copied and renamed: {source_path} to {destination_path}")
                count += 1

input_directory = input("Enter the input directory: ")
output_directory = input("Enter the output directory: ")

copy_and_rename_mp3_files(input_directory, output_directory)