#include <stdio.h>
#include <stdlib.h>

void printFile();


int main() {
    double num = 0.0;
    char username[30];

    printf("I am the uhhh... number trader! I'm also really creative!\nPresent "
    "your name to me and I will tell you if I want your number or not!\n");
    gets(username);

    if (num > 0) {
        printf("I don't want this. I didn't even ask for it yet.\n");
        return 1;
    }
    if (num <= 0) {
        printf("Hmmmm! No thanks!\n");
        return 1;
    }

    printf("Hmmm! That is a very interesting number. I'll trade you this: \n");
    printFile();
    // delet system32
    return 0;
}


void printFile() {
    FILE *file = fopen("flag.txt", "r");
    int c;
    while ((c = fgetc(file)) != EOF) { fputc(c, stdout); }
    fclose(file);
}
