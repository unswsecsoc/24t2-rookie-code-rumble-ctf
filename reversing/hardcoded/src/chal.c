#include <stdio.h>
#include <stdlib.h>

int xorFunction(int data, int key);
void printArray(int* arr, int size);
int *openFile(int *maxInd);


int main() {
    printf("\"Encrypting...\"\nInput: <REDACTED>\n");

    int maxInd = 0;
    int *data = openFile(&maxInd);

    for (int i = 0; i < maxInd; i++) {
        data[i] = xorFunction(data[i], data[maxInd-i-1]);
    }

    printArray(data, maxInd);
    free(data);
    return 0;
}



// Helper functions ////////////////////////////////////////////////////////////

int xorFunction(int data, int key) {
    return data^key;
}


void printArray(int* arr, int size) {
    printf("Data \"Encrypted\"!\nOutput: \n");
    for (int i = 0; i < size; i++) {
        printf("%X ", arr[i]);
    }
    printf("\n");
}


int* openFile(int *maxInd) {
    FILE *file = fopen("source.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(1);
    }

    // Find the file size
    fseek(file, 0, SEEK_END);
    long fileSize = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allocate memory to store the file contents
    int *data = malloc(fileSize * sizeof(int));
    if (data == NULL) {
        perror("Memory allocation failed");
        fclose(file);
        exit(1);
    }

    // Read the file contents into the data array
    int i = 0;
    for (; i < fileSize; i++) {
        data[i] = fgetc(file);
    }
    *maxInd = i;

    fclose(file);
    return data;
}
