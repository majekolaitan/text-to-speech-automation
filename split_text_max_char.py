import os

def remove_empty_lines(text):
    """
    Remove empty lines from the input text.
    An empty line is considered a line containing only whitespace characters
    (space, tab, newline, etc.).
    """
    lines = text.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    cleaned_text = '\n'.join(non_empty_lines)
    return cleaned_text

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

    # Remove empty lines from the input text
    cleaned_text = remove_empty_lines(text)

    # Define sentence-ending punctuation marks
    end_punctuation = ['.', '?', '!']

    # Initialize variables
    start = 0
    end = max_chars
    file_count = 1
    total_char_count = 0

    while start < len(cleaned_text):
        # Check if the end index is within the bounds of the string
        if end <= len(cleaned_text):
            # Check if the last character is a sentence-ending punctuation mark
            if cleaned_text[end - 1] in end_punctuation:
                # Write the text to an output file
                output_file = os.path.join(output_folder, f'output_{file_count}.txt')
                with open(output_file, 'w') as out_file:
                    file_text = cleaned_text[start:end]
                    out_file.write(file_text)
                    file_char_count = len(file_text)
                    total_char_count += file_char_count
                    print(f"File '{output_file}' has {file_char_count} characters.")

                # Update the start and end indices for the next file
                start = end
                end = start + max_chars
            else:
                # Find the nearest sentence-ending punctuation mark backward
                while end > start and cleaned_text[end - 1] not in end_punctuation:
                    end -= 1

                # Write the text up to the found punctuation mark to an output file
                output_file = os.path.join(output_folder, f'output_{file_count}.txt')
                with open(output_file, 'w') as out_file:
                    file_text = cleaned_text[start:end]
                    out_file.write(file_text)
                    file_char_count = len(file_text)
                    total_char_count += file_char_count
                    print(f"File '{output_file}' has {file_char_count} characters.")

                # Update the start and end indices for the next file
                start = end
                end = start + max_chars

            # Update the file count
            file_count += 1
        else:
            # If the end index is out of bounds, write the remaining text to a file
            output_file = os.path.join(output_folder, f'output_{file_count}.txt')
            with open(output_file, 'w') as out_file:
                file_text = cleaned_text[start:]
                out_file.write(file_text)
                file_char_count = len(file_text)
                total_char_count += file_char_count
                print(f"File '{output_file}' has {file_char_count} characters.")
            break

    # Print the total character count across all output files
    print(f"Total characters across all output files: {total_char_count}")

    # Verify the total character count with the input file
    input_char_count = len(cleaned_text)
    if total_char_count == input_char_count:
        print("The total character count across all output files matches the input file.")
    else:
        print("The total character count across all output files does not match the input file.")

# Example usage
input_file = 'input.txt'
output_folder = 'output'
copy_text_to_files(input_file, output_folder)