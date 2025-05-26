import sys
import os
import shutil

def main():
    # Ensure the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./problem1 input.txt output.txt \"hello world\"")
        sys.exit(1)

    # Parse command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    append_string = sys.argv[3]

    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        sys.exit(1)

    try:
        # Check file size and create a backup if over 1MB
        file_size = os.path.getsize(input_file)
        if file_size > 1 * 1024 * 1024:  # 1MB in bytes
            backup_file = input_file + ".bak"
            shutil.copy2(input_file, backup_file)
            print(f"Backup created: {backup_file}")

        # Read the input file contents
        with open(input_file, 'r') as infile:
            contents = infile.read()

        # Append the string to the contents
        updated_contents = contents + append_string

        # Write to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(updated_contents)

        # Display the updated contents
        print("Updated contents of the output file:")
        print(updated_contents)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()