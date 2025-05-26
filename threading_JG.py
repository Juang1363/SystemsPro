import threading

# Global shared counter and lock
counter = 0
mutex = threading.Lock()

# Increment function
def increment_steps(steps):
    global counter
    for _ in range(steps):
        mutex.acquire()
        try:
            counter += 1
        finally:
            mutex.release()

# Decrement function
def decrement_steps(steps):
    global counter
    for _ in range(steps):
        mutex.acquire()
        try:
            counter -= 1
        finally:
            mutex.release()

def main():
    global counter
    steps_per_thread = 100_000_000  # Each thread will handle this many steps

    # Incrementing phase
    print("Starting incrementing threads...")
    increment_threads = []
    for _ in range(10):
        thread = threading.Thread(target=increment_steps, args=(steps_per_thread,))
        increment_threads.append(thread)
        thread.start()

    for thread in increment_threads:
        thread.join()  # Wait for all threads to complete

    print(f"Counter after incrementing: {counter}")

    # Decrementing phase
    print("Starting decrementing threads...")
    decrement_threads = []
    for _ in range(10):
        thread = threading.Thread(target=decrement_steps, args=(steps_per_thread,))
        decrement_threads.append(thread)
        thread.start()

    for thread in decrement_threads:
        thread.join()  # Wait for all threads to complete

    print(f"Counter after decrementing: {counter}")

if __name__ == "__main__":
    main()
