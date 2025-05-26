#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <errno.h>
#include <string.h>
#define PID_MAX_FILE "/proc/sys/kernel/pid_max"
//P.S each function has a close file function in case of an error as well.
//This function just handles if theres an error within the program.
void handle_error(const char *function_name) {
    fprintf(stderr, "Error in %s: %s\n", function_name, strerror(errno));
    exit(EXIT_FAILURE);
}
//Reads the current max PID, opens the file in read mode, reads and converts the content to a long for file operations for numerical operations
long fetch_pid_max() {
    FILE *fp = fopen(PID_MAX_FILE, "r");
    if (fp == NULL) {
        handle_error("fopen (read)");
    }

    char buffer[32];
    if (fgets(buffer, sizeof(buffer), fp) == NULL) {
        fclose(fp);
        handle_error("fgets (read)");
    }

    fclose(fp);
    return strtol(buffer, NULL, 10);
}
//Updates PID max to a new value and writes the new values into the new file.
void update_pid_max(long new_value) {
    FILE *fp = fopen(PID_MAX_FILE, "w");
    if (fp == NULL) {
        handle_error("fopen (write)");
    }

    if (fprintf(fp, "%ld\n", new_value) < 0) {
        fclose(fp);
        handle_error("fprintf (write)");
    }

    fclose(fp);
}
//Checks if one argument if not gives an error, and converts the command line argument into a long.
int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <desired_pid_max>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    long desired_pid_max = atol(argv[1]);
    if (desired_pid_max <= 0) {
        fprintf(stderr, "Invalid pid_max value: %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }
    //THE CHILD IS ALIVE!!!(Faker refrence). We basically create a child using fork. The rest handles stuff with the parent process and outputs the current PID value and updates the /proc/sys/kernel/pid_max
    pid_t child_pid = fork();
    if (child_pid < 0) {
        handle_error("fork");
    } else if (child_pid == 0) { // Child process
        printf("Child process: Fetching current pid_max...\n");
        long current_pid_max = fetch_pid_max();
        printf("Child process: Current pid_max is %ld\n", current_pid_max);

        if (desired_pid_max > current_pid_max) {
            fprintf(stderr, "Child process: Desired pid_max (%ld) exceeds current pid_max (%ld)\n", desired_pid_max, current_pid_max);
            exit(EXIT_FAILURE);
        }

        printf("Child process: Updating pid_max to %ld...\n", desired_pid_max);
        update_pid_max(desired_pid_max);
        printf("Child process: pid_max successfully updated.\n");

        exit(EXIT_SUCCESS);
    } else { // Parent process
        if (waitpid(child_pid, NULL, 0) < 0) {
            handle_error("waitpid");
        }

        printf("Parent process: Reading updated pid_max...\n");
        long updated_pid_max = fetch_pid_max();
        printf("Parent process: Updated pid_max is %ld\n", updated_pid_max);

        return EXIT_SUCCESS;
    }
}

