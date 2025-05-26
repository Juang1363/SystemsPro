#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <errno.h>

// Signal handler for the child process
void child_signal_handler(int sig) {
    if (sig == SIGUSR1) {
        printf("Child received SIGUSR1!\n");
    }
}

// Signal handler for the parent process
void parent_signal_handler(int sig) {
    if (sig == SIGUSR2) {
        printf("Parent received SIGUSR2!\n");
    }
}

int main() {
    pid_t pid;
    struct sigaction sa;
    sigset_t mask;

    // Block SIGUSR1 and SIGUSR2 initially
    sigemptyset(&mask);
    sigaddset(&mask, SIGUSR1);
    sigaddset(&mask, SIGUSR2);
    if (sigprocmask(SIG_BLOCK, &mask, NULL) == -1) {
        perror("sigprocmask");
        exit(EXIT_FAILURE);
    }

    // Forking the child process
    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) { // Child Process
        // Unblock SIGUSR1 in the child
        sigemptyset(&mask);
        if (sigprocmask(SIG_SETMASK, &mask, NULL) == -1) {
            perror("sigprocmask (child)");
            exit(EXIT_FAILURE);
        }

        // Set up signal handler for SIGUSR1 in the child
        sa.sa_handler = child_signal_handler;
        sigemptyset(&sa.sa_mask);
        sa.sa_flags = 0;
        if (sigaction(SIGUSR1, &sa, NULL) == -1) {
            perror("sigaction (child) SIGUSR1");
            exit(EXIT_FAILURE);
        }

        // Wait for SIGUSR1 from the parent
        pause();

        // Send SIGUSR2 to the parent
        if (kill(getppid(), SIGUSR2) == -1) {
            perror("kill SIGUSR2");
            exit(EXIT_FAILURE);
        }

        printf("Goodbye from Child (PID: %d)\n", getpid());
        exit(EXIT_SUCCESS);

    } else { // Parent Process
        // Set up signal handler for SIGUSR2 in the parent
        sa.sa_handler = parent_signal_handler;
        sigemptyset(&sa.sa_mask);
        sa.sa_flags = 0;
        if (sigaction(SIGUSR2, &sa, NULL) == -1) {
            perror("sigaction (parent) SIGUSR2");
            exit(EXIT_FAILURE);
        }

        printf("Parent started...\n");
        sleep(3); // Simulate some delay
        printf("Parent about to signal child...\n");

        // Send SIGUSR1 to the child
        if (kill(pid, SIGUSR1) == -1) {
            perror("kill SIGUSR1");
            exit(EXIT_FAILURE);
        }

        // Unblock SIGUSR2 and wait for it
        sigemptyset(&mask);
        if (sigsuspend(&mask) == -1 && errno != EINTR) {
            perror("sigsuspend");
            exit(EXIT_FAILURE);
        }

        printf("Goodbye from Parent (PID: %d)\n", getpid());
        exit(EXIT_SUCCESS);
    }
}

