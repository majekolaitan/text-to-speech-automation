import os
import re

def split_text_heading(input_file, output_folder, heading_regex):

    with open(input_file, 'r') as file:
        text = file.read()

    matches = re.finditer(heading_regex, text, re.DOTALL)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write each match to a text file in the output folder
    for i, match in enumerate(matches, start=1):
        lesson_content = match.group(0)
        output_file = os.path.join(output_folder, f"Lesson_{i}.txt")
        with open(output_file, 'w') as f:
            f.write(lesson_content.strip())