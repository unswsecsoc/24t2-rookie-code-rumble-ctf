#include <stdio.h>

int main() {

    int numbers[10];
    for (int i = 0; i < 10; i++) {
        numbers[i] = i + 1;
    }

    for (int i = 0; i < 10; i++) {
        if (numbers[i] % 3 == 0 && numbers[i] % 5 == 0) {
            numbers[i] = 0;
        } else if (numbers[i] % 3 == 0) {
            numbers[i] = 0;
        } else if (numbers[i] % 5 == 0) {
            numbers[i] = 0;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", numbers[i]);
    }

    printf("\n");

    return 0;
}