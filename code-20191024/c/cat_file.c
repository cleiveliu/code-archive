#include <stdio.h>

int main(int argc, char *argv[]) {
    FILE *fp;
    void filecopy(FILE *, FILE *);

    if (argc == 1) {
        filecopy(stdin, stdout);
    } else {
        while (--argc > 0) {
            if ((fp = fopen(*(++argv), "r")) == NULL) {
                printf("can't open file %s\n", *argv);
                return 1;
            } else {
                filecopy(fp, stdout);
                putchar('\n');
                fclose(fp);
            }
        }
    }
    return 0;
}

void filecopy(FILE *in, FILE *out) {
    int c;
    while ((c = getc(in)) != EOF) {
        putc(c, out);
    }
}