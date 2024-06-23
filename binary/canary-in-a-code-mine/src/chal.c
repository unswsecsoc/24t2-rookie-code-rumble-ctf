#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int checkIfA(char *username, char *password);
void printFile();

int main() {
    int admin = 0;
    char protect[] = {'\0', 'A'};
    char username[10];
	char password[5];

    printf("This is THE mining company's employee portal.\n");
    printf("---------------------------------------------\n");
	printf("Please enter your name:\n");
    gets(username);
    printf("Please enter your password:\n");
    gets(password);


    if (strcmp(username, "AAAAAAAAAA") == 0 || strcmp(password, "AAAAA") == 0) {
        printf("What a strange username or password!\n");
        return 1;
    }

    if (admin != 0 && protect[0] == '\0' && protect[1] == 'A') {
        printf("Welcome admin!\n");
        printFile();
        return 0;
    }

    printf("Employee not found!\n");
    return 1;
}

void printFile() {
    FILE *file = fopen("flag.txt", "r");
    int c;
    while ((c = fgetc(file)) != EOF) { fputc(c, stdout); }
    fclose(file);
}
