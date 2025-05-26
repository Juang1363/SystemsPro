#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 65432
#define BUFFER_SIZE 1024

int main() {
    int server_fd, client_fd;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_len = sizeof(client_addr);
    char buffer[BUFFER_SIZE];
    const char *hello_response = "world";
    const char *exit_response = "exit";

    // Create socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Configure server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    // Bind socket
    if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Bind failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    // Listen for connections
    if (listen(server_fd, 1) == -1) {
        perror("Listen failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Server is listening on port %d...\n", PORT);

    // Accept client connection
    if ((client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &addr_len)) == -1) {
        perror("Accept failed");
        close(server_fd);
        exit(EXIT_FAILURE);
    }

    printf("Connection established with client.\n");

    while (1) {
        memset(buffer, 0, BUFFER_SIZE);

        // Receive message from client
        ssize_t bytes_received = recv(client_fd, buffer, BUFFER_SIZE, 0);
        if (bytes_received <= 0) {
            perror("Receive failed");
            break;
        }

        printf("Msg received from client: %s\n", buffer);

        // Respond based on message
        if (strncmp(buffer, "hello", 5) == 0) {
            send(client_fd, hello_response, strlen(hello_response), 0);
            printf("Responding with: %s\n", hello_response);
        } else if (strncmp(buffer, "exit", 4) == 0) {
            send(client_fd, exit_response, strlen(exit_response), 0);
            printf("Responding with: %s\n", exit_response);
            break;
        } else {
            const char *unknown_response = "Unknown command";
            send(client_fd, unknown_response, strlen(unknown_response), 0);
            printf("Responding with: %s\n", unknown_response);
        }
    }

    printf("closing connection\n");

    // Clean up
    close(client_fd);
    close(server_fd);

    return 0;
}
