#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "shared_file.txt"
#define BUFFER_SIZE 1024

void parent_process() {
    FILE *file = fopen(FILENAME, "w+");
    if (file == NULL) {
        perror("fopen failed");
        exit(1);
    }
    const char *message = "Hello from Parent Process!";
    fprintf(file, "%s\n", message);
    fflush(file);
    fclose(file);
    printf("Parent: Written to file.\n");
}

void child_process() {
    FILE *file = fopen(FILENAME, "r");
    if (file == NULL) {
        perror("fopen failed");
        exit(1);
    }
    char buffer[BUFFER_SIZE];
    if (fgets(buffer, BUFFER_SIZE, file) != NULL) {
        printf("Child: Read from file: %s\n", buffer);
    } else {
        perror("fgets failed");
    }
    fclose(file);
}

int main() {
    parent_process();
    child_process();
    if (remove(FILENAME) == 0) {
        printf("Parent: File cleaned up.\n");
    } else {
        perror("remove failed");
    }
    return 0;
}