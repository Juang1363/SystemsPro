#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdio.h>
#include <sys/stat.h>

int copy_file(const char *source, const char *destination) {
    char buffer[100];
    ssize_t bytes_read, bytes_written;

    // Open source file for reading
    int read_fd = open(source, O_RDONLY);
    if (read_fd == -1) {
        perror("Error opening source file");
        printf("errno: %d\n", errno); // Print errno for debugging
        return -1; // Return -1 on failure
    }

    // Open destination file for writing
    int write_fd = open(destination, O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
    if (write_fd == -1) {
        perror("Error opening destination file");
        printf("errno: %d\n", errno); // Print errno for debugging
        close(read_fd);  // Close the source file
        return -1;       // Return -1 on failure
    }

    // Read from source file and write to destination file
    while ((bytes_read = read(read_fd, buffer, sizeof(buffer))) > 0) {
        bytes_written = write(write_fd, buffer, bytes_read);
        if (bytes_written == -1) {
            perror("Error writing to destination file");
            printf("errno: %d\n", errno); // Print errno for debugging
            close(read_fd);
            close(write_fd);
            return -1; // Return -1 on failure
        }
    }

    if (bytes_read == -1) {
        perror("Error reading from source file");
        printf("errno: %d\n", errno); // Print errno for debugging
        close(read_fd);
        close(write_fd);
        return -1; // Return -1 on failure
    }

    // Close both files
    close(read_fd);
    close(write_fd);

    return 0; // Success
}


