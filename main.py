import os
import shutil
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError

def get_mp3_duration(file_path):
    try:
        audio = AudioSegment.from_file(file_path, format="mp3")
        return len(audio) / 1000  # Duration in seconds
    except CouldntDecodeError:
        return 0  # Return 0 if the file couldn't be decoded

def copy_and_rename_mp3_files(input_dir, output_dir):
    count = 1
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                duration = get_mp3_duration(file_path)
                if duration >= 5:
                    destination_path = os.path.join(output_dir, f"{count}.mp3")
                    shutil.copy2(file_path, destination_path)
                    print(f"Copied and renamed: {file_path} to {destination_path}")
                    count += 1

input_directory = input("Enter the input directory: ")
output_directory = input("Enter the output directory: ")

copy_and_rename_mp3_files(input_directory, output_directory)
