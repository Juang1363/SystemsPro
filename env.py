import os
import sys

def main():
    # Retrieve the value of the EXAM_MODE environment variable
    exam_mode = os.environ.get("EXAM_MODE")

    if exam_mode == "debug":
        # If EXAM_MODE is set to 'debug', print the current process ID and parent process ID
        current_pid = os.getpid()
        parent_pid = os.getppid()
        print(f"Debug Mode Enabled:\n  Process ID: {current_pid}\n  Parent Process ID: {parent_pid}")
    else:
        # If EXAM_MODE is not set or set to a value other than 'debug', set it to 'release'
        os.environ["EXAM_MODE"] = "release"
        print("EXAM_MODE was not set to 'debug'. Setting it to 'release' and exiting.")
        sys.exit(0)  # Exit the program gracefully

if __name__ == "__main__":
    main()