def split_file(input_file, chunk_size):
    with open(input_file, 'r') as f:
        data = f.read()
        chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    for i, chunk in enumerate(chunks):
        output_file = f"{input_file}_part{i+1}.txt"
        with open(output_file, 'w') as f:
            f.write(chunk)

# Example usage:
input_file = 'input.txt'
chunk_size = 1000  # Adjust this value as needed
split_file(input_file, chunk_size)
