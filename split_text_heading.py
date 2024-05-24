import os
import re

# Define the regex pattern
pattern = r'\nLesson\s.*?(?=\nLesson\s|\Z)'

# Read input text from a file
file_path = 'input.txt'
with open(file_path, 'r') as file:
    text = file.read()

# Find all matches
matches = re.finditer(pattern, text, re.DOTALL)

# Create output folder if it doesn't exist
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Write each match to a text file in the output folder
for i, match in enumerate(matches, start=1):
    lesson_content = match.group(0)
    output_file = os.path.join(output_folder, f"Lesson_{i}.txt")
    with open(output_file, 'w') as f:
        f.write(lesson_content.strip())
