from sys import argv
import hashlib

# Reading file content in 32KB chunks
BUF_SIZE = 32768

# Function to check if the entered hash algorithm is valid
def check_valid_hash_algo(argument_hash):
    valid_hash_algos = hashlib.algorithms_available
    return argument_hash in valid_hash_algos

# Function to compute the hash of a file
def compute_file_hash(filepath, hash_func):
    try:
        # Open file in binary read mode
        with open(filepath, 'rb') as read_file:
            while True:
                data = read_file.read(BUF_SIZE)
                if not data:
                    break
                # Update the hash with the data chunk
                hash_func.update(data)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return None

# Main code to execute the program
if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 hash_first_lastname.py input_file.txt [hash-algorithm]")
        exit(1)

    filepath = argv[1]
    hash_algorithm = argv[2] if len(argv) > 2 else "sha256"

    if not check_valid_hash_algo(hash_algorithm):
        print(f"Invalid hash algorithm '{hash_algorithm}', falling back to default 'sha256'.")
        hash_algorithm = "sha256"

    # Get the hash function
    try:
        hash_func = getattr(hashlib, hash_algorithm)()
    except AttributeError:
        print(f"Error: Could not initialize hash algorithm '{hash_algorithm}'.")
        exit(1)

    # Compute the file hash
    file_hash = compute_file_hash(filepath, hash_func)
    if file_hash:
        # Write the hash to output.txt
        try:
            with open("output.txt", "w") as write_file:
                write_file.write(file_hash + "\n")
            print(f"Hash computed successfully using '{hash_algorithm}'. Result saved in 'output.txt'.")
        except Exception as e:
            print(f"Error: Unable to write to 'output.txt' - {e}")
