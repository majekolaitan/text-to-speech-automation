import os

def copy_text_to_files(input_file, output_folder, max_chars=4800):
    """
    Recursively copy text from an input file to output files in a specified folder.
    Each output file will contain up to max_chars characters.
    If the last character is not a sentence-ending punctuation mark, look backward
    to the nearest such punctuation mark.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the input file
    with open(input_file, 'r') as f:
        text = f.read()

    # Define sentence-ending punctuation marks
    end_punctuation = ['.', '?', '!']

    # Initialize variables
    start = 0
    end = max_chars
    file_count = 1

    while start < len(text):
        # Check if the end index is within the bounds of the string
        if end <= len(text):
            # Check if the last character is a sentence-ending punctuation mark
            if text[end - 1] in end_punctuation:
                # Write the text to an output file
                with open(os.path.join(output_folder, f'output_{file_count}.txt'), 'w') as out_file:
                    out_file.write(text[start:end])
            else:
                # Find the nearest sentence-ending punctuation mark backward
                while end > start and text[end - 1] not in end_punctuation:
                    end -= 1

                # Write the text up to the found punctuation mark to an output file
                with open(os.path.join(output_folder, f'output_{file_count}.txt'), 'w') as out_file:
                    out_file.write(text[start:end])

                # Update the start and end indices for the next file
                start = end
                end = start + max_chars

            # Update the file count
            file_count += 1
        else:
            # If the end index is out of bounds, write the remaining text to a file
            with open(os.path.join(output_folder, f'output_{file_count}.txt'), 'w') as out_file:
                out_file.write(text[start:])
            break

# Example usage
input_file = 'input.txt'
output_folder = 'output'
copy_text_to_files(input_file, output_folder)