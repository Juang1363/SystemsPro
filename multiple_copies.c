//Juan E Gonzalez UTSA ID:Mzr718
#include <stdio.h>
#include <stlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argumentc, char *argumentv[]) {
// This is done so that that the command can go through if its 4
if (argumentc != 4) {
fprintf(stderr, "Usage: %s source_file destination_file1 destination_file2\
n", argumentv[0]);
return 1;
}
// We gotta open the source file in order to copy it over.
int source_file = open(argumentv[1], O_RDONLY);
if (source_file < 0) {
fprintf(stderr, "Opening Error with the source file!: %s\n", argumentv[1]);
return 1;
}
// We gotta open the destination file 1 so that we can write in it.
int destination_file1 = open(argumentv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
if (destination_file1 < 0) {
fprintf(stderr, "Opening Error with the destination file 1!: %s\n",
argumentv[2]);
close(source_file);
return 1;
}
// We gotta open the destination file 2 so that we can write in it.
int destination_file2 = open(argumentv[3], O_WRONLY | O_CREAT | O_TRUNC, 0644);
if (destination_file2 < 0) {
fprintf(stderr, "Opening Error with the destination file 2!: %s\n",
argumentv[3]);
close(source_file);
close(destination_file1);
return 1;
}
// We need this buffer in order for these commands to go through.
char buffer[1024];
ssize_t bytesRead;
// This does the actually copying of the source file into the destination
files.
while ((bytesRead = read(source_file, buffer, sizeof(buffer))) > 0) {
write(destination_file1, buffer, bytesRead);
write(destination_file2, buffer, bytesRead);
}
// We finally close the files since we don't need them anymore.
close(source_file);
close(destination_file1);
close(destination_file2);
printf("You now have mutiple copies of the source file!\n");
return 0;
}