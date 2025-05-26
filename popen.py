import subprocess
import sys

def main():
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <message> <filename>")
        sys.exit(1)
    
    # Command-line arguments
    message = sys.argv[1]
    filename = sys.argv[2]

    # Part a: Write the message to the specified file using echo and Popen
    print(f"Using popen to echo '{message}' to a file")
    echo_process = subprocess.Popen(["echo", message], stdout=subprocess.PIPE, text=True)
    output, _ = echo_process.communicate()
    with open(filename, "w") as file:
        file.write(output.strip())  # Write the echoed output to the file manually

    # Part b: Read the contents of the specified file using cat and Popen
    print(f"Using popen to cat {filename}")
    cat_process = subprocess.Popen(["cat", filename], stdout=subprocess.PIPE, text=True)
    cat_output, _ = cat_process.communicate()
    print(f"Contents of {filename}: {cat_output.strip()}")

if __name__ == "__main__":
    main()
