import threading

# Global variables shared by threads
data = list(range(500))   # List of numbers
partial_sums = [0] * 5    # List to hold results of partial sums

# A lock to control access to shared resources
thread_lock = threading.Lock()

def calculate_partial_sum(segment_index):
    # Compute sum of one segment of data
    segment_sum = sum(data[segment_index * 100:(segment_index + 1) * 100])
    
    # Acquire the lock to safely update the shared list
    with thread_lock:
        partial_sums[segment_index] = segment_sum
        current_thread = threading.get_ident()
        # Updated print statement as per your request
        print(f"Accumulated value in thread [{current_thread} -> {segment_index}] is {segment_sum}")

def main():
    threads = []
    
    # Create threads to calculate partial sums
    for segment in range(5):
        thread = threading.Thread(target=calculate_partial_sum, args=(segment,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    # Calculate the total sum from all segments
    grand_total = sum(partial_sums)
    print(f"Total is: {grand_total}")

if __name__ == '__main__':
    main()
