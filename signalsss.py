import os
import signal
import time

def child_handler(signum, frame):
    """Handler for the child process to catch signals."""
    if signum == signal.SIGUSR1:
        print(f"Child process received SIGUSR1. PID: {os.getpid()}, PPID: {os.getppid()}.")
        exit(0)
    else:
        print(f"Child process received unexpected signal: {signum}. Gracefully ignoring.")

def main():
    try:
        pid = os.fork()
    except OSError as e:
        print(f"Fork failed: {e}")
        return

    if pid == 0:
        # Child process
        print(f"Child process started. PID: {os.getpid()}, waiting for SIGUSR1.")
        signal.signal(signal.SIGUSR1, child_handler)
        signal.signal(signal.SIGINT, child_handler)  # Handling Ctrl+C as an example of unexpected signal
        while True:
            signal.pause()  # Wait for a signal
    else:
        # Parent process
        print(f"Parent process. PID: {os.getpid()}, sending SIGUSR1 to child (PID: {pid}) after 5 seconds.")
        time.sleep(5)
        os.kill(pid, signal.SIGUSR1)
        print("Parent sent SIGUSR1 to child.")
        os.wait()  # Wait for the child process to terminate
        print("Parent process: Child has terminated.")

if __name__ == "__main__":
    main()
