#include <stdio.h>


int main(int argc, char *argv[]) {
    int i;
    printf("%s\n", argv[0]);
    for (i=1; i < argc; i++) {
        printf("%s%s",argv[i], i< argc? " ":"");
    }
    printf("\n");
    return 0;
}