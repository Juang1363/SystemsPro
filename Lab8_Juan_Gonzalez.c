//You only need these headers in your code:
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
int main() {
    // Attempt to create a new child process
    pid_t child_process_id = fork();
    
    // Assess the outcome of fork()
    if (child_process_id < 0) {
        // If fork failed, display an error and exit
        perror("Error: fork failed");
        _exit(1);  // Exit with failure code
    } else if (child_process_id == 0) {
        // Code executed only by the child process
        sleep(1); // Delay for 1 second before printing
        printf("[PID %d] Child process. Parent PID = %d.\n", (int)getpid(), (int)getppid());
        _exit(0);  // Successful exit for child
    }
    
    // Code executed only by the parent process
    printf("[PID %d] Parent process. Child PID = %d.\n", (int)getpid(), (int)child_process_id);
    _exit(0);  // Successful exit for parent
}

