import os

def find_sentence_boundary(chunk):
    # Find the last occurrence of '.', '?', or '!' to split the chunk
    for i in range(len(chunk) - 1, -1, -1):
        if chunk[i] in ['.', '?', '!']:
            return i + 1  # Include the punctuation
    return None

def split_file(input_file, max_chars):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    chunks = []
    current_chunk = ""
    current_length = 0
    for line in lines:
        if current_length + len(line) <= max_chars:
            current_chunk += line
            current_length += len(line)
        else:
            boundary_index = find_sentence_boundary(current_chunk)
            if boundary_index is not None:
                chunks.append(current_chunk[:boundary_index].strip())
                current_chunk = current_chunk[boundary_index:]
                current_length = len(current_chunk)
            else:
                chunks.append(current_chunk.strip())
                current_chunk = line
                current_length = len(line)

    # Add the last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Write chunks to files
    for i, chunk in enumerate(chunks):
        output_file = f"{os.path.splitext(input_file)[0]}_part{i+1}.txt"
        with open(output_file, 'w') as f:
            f.write(chunk)

# Example usage:
input_file = 'input.txt'
max_chars = 1000  # Adjust this value as needed
split_file(input_file, max_chars)
