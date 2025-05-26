#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    // Step 1./assignment3 <your_student_id>
    // Pass in your student id via command line argument.
    // Set environment variable USER_ID to your student ID.
    // Print USER_ID
    printf("Student ID: %s\n", argv[1]); 
    if (setenv("USER_ID", argv[1], 1) != 0) {
    perror("Failure to set USER_ID");
    } 
    char *env_results2 = getenv("USER_ID");
    printf("USER_ID: %s\n", env_results2);
    // Step 2
    // Set environment variable ASSIGNMENT3 to "Environment Variables and Process IDs"
    // Print ASSIGNMENT3
    int result = putenv("ASSIGNMENT3=Environment Variables and Process IDs");
    if (result == -1)
    {
    printf("Error checking putenv");
    return -1;
    }
    char *env_results = getenv("ASSIGNMENT3");
    printf("ASSIGNMENT3: %s\n", env_results);
    // Step 3
    // Write code to get your process's ID (PID)
    // Example code to convert int to char[]
    // char pid_str[8] = {0};
    // sprintf(pid_str, "%d", <variable used for getpid>);
    char buff[10] = {0};
    int pid = getpid();
    sprintf(buff, "%d", pid);
    printf("my process id is: %s\n", buff);

    // Step 4
    // Set environment variable MY_PID to the PID found above
    // Print the PID
    setenv("MY_PID", buff,1); 
    printf("MY_PID: %s\n", getenv("MY_PID"));
    // Step 5
    // An environment variable named "COURSE_NAME" is available
    // Print the value
    // Change it to the correct course name (EE3233 Systems Programming)
    // Print it again
    char *course_name = getenv("COURSE_NAME");
    if (course_name) {
        printf("COURSE_NAME before update: %s\n", course_name);
    } else {
        printf("COURSE_NAME is not set.\n");
    }
    setenv("COURSE_NAME", "EE3233 Systems Programming", 1); 
    printf("COURSE_NAME after update: %s\n", getenv("COURSE_NAME"));
    return 0;
}