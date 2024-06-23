#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int admin = 0;
    int stock[3];
    int *age = malloc(sizeof(*age));

    printf("hell o welcome to my creep stand REEE\n");
    printf("her'es our stock\n");

    for (int i = 1; i <= 3; i++) {
        printf("crep %d: %ld\n", i, stock+i); // pointer arithmetic ;)
    }

    printf("ok uh what's your age\n");
    fscanf(stdin, "%ld", &age);
    printf("nah that's an awful age lmao\n");

    srandom(time(NULL));
    *age = random();
    printf("you are now %d years old\n", *age);

    printf("rip we're out of stock\n");
    if (admin) {
        printf("oh you're my employer haha nice take this crepe:\n");

        FILE *f = fopen("flag.txt", "rb");
        int c;

        while ((c = fgetc(f)) != EOF) {
            putchar(c);
        }

        fclose(f);
    }
}