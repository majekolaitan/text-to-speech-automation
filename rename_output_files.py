import os
import re
from pathlib import Path

# Define the directory containing the files
directory = "output"

# Get a list of all files in the directory
files = os.listdir(directory)

# Sort the files numerically
files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

# Initialize the current_section and part variables
current_section = None
part_number = 0

# Loop through each file
for filename in files:
    # Construct the full file path
    file_path = os.path.join(directory, filename)

    # Open the file and read its contents
    with open(file_path, "r") as f:
        contents = f.readlines()

    # Flag to track if a section was found in the file
    section_found = False

    # Loop through each line in the file
    for line in contents:
        # Check if the line starts with "Section" followed by a number
        match = re.match(r"^Section (\d+)", line)
        if match:
            section_found = True
            # Extract the section number
            section_number = int(match.group(1))

            # Update the current_section variable if necessary
            if current_section is None or section_number > current_section:
                current_section = section_number
                part_number = 1
                print(f"Found Section {current_section} in file {filename}")

    # Rename the file with the section and part number
    if section_found:
        new_filename = f"Section {current_section} - Part 1.txt"
    else:
        part_number += 1
        new_filename = f"Section {current_section} - Part {part_number}.txt"

    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)