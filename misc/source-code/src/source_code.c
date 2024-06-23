#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  char *source_code_filename = strcat(argv[0], ".c");
  
  FILE *fptr = fopen(source_code_filename, "r");

  if (fptr == NULL) {
    printf("Error: cannot open the file.\n");
    exit(1);
  }

  char c = fgetc(fptr); 
  while (c != EOF) {
    printf("%c", c); 
    c = fgetc(fptr);
  } 

  putchar('\n');
  fclose(fptr);

  return 0;
}