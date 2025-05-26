#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// Shared total sum and mutex for thread safety
long long total_sum = 0;
pthread_mutex_t sum_mutex;

// Function executed by each thread
void *calculate_sum(void *arg) {
    int n = *(int *)arg;
    long long partial_sum = (n * (n + 1)) / 2; // Calculate sum from 1 to n

    // Lock the mutex before updating the shared total
    pthread_mutex_lock(&sum_mutex);
    total_sum += partial_sum;
    pthread_mutex_unlock(&sum_mutex);

    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <number_of_threads>\n", argv[0]);
        return EXIT_FAILURE;
    }

    int n = atoi(argv[1]);

    // Validate the input
    if (n < 1) {
        fprintf(stderr, "Error: Number of threads must be >= 1\n");
        return EXIT_FAILURE;
    }

    pthread_t threads[n];

    // Initialize the mutex
    if (pthread_mutex_init(&sum_mutex, NULL) != 0) {
        fprintf(stderr, "Error: Mutex initialization failed\n");
        return EXIT_FAILURE;
    }

    // Create threads
    for (int i = 0; i < n; i++) {
        if (pthread_create(&threads[i], NULL, calculate_sum, &n) != 0) {
            fprintf(stderr, "Error: Failed to create thread %d\n", i);
            return EXIT_FAILURE;
        }
    }

    // Wait for threads to complete
    for (int i = 0; i < n; i++) {
        pthread_join(threads[i], NULL);
    }

    // Destroy the mutex
    pthread_mutex_destroy(&sum_mutex);

    // Print the total sum
    printf("Total sum calculated by %d threads: %lld\n", n, total_sum);

    return EXIT_SUCCESS;
}
