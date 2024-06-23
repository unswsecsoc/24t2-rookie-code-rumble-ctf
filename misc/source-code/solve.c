#include <unistd.h>

int main(void) {
  execl("./source_code", "flag", NULL);
  return 0;
}

// Or alternatively, `exec -a flag ./source_code` in CLI