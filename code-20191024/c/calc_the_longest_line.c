#include <stdio.h>

#define MAXSIZE 1000

int getlinee(char s[], int lim);
void copy(char to[], char from[]);

int main() {
    int len = 0;
    int max = 0;
    char line[MAXSIZE];
    char longest[MAXSIZE];
    len = getlinee(line, MAXSIZE);
    while (len > 0) {
        if (len > max) {
            max = len;
            copy(longest, line);
        }
        len = getlinee(line, MAXSIZE);
    }

    if (max > 0) {
        printf("the max length is %d\n", max);
    }
    printf("the content is:\n");
    int i = 0;
    while(longest[i] != '\0' && i < 4) {
        putchar(longest[i]);
        i += 1;
    }
}


int getlinee(char line[], int limit) {
    char c;
    int i = 0;
    c = getchar();
    while (i < limit - 1 && c != EOF && c != '\n') {
        line[i] = c;
        i += 1;
        c = getchar();
    }
    if (c == '\n') {
        line[i] = c;
        i += 1;
    }
    line[i] = '\0';
    return i;
}


void copy(char to[], char from[]) {
    int i = 0;
    while (from[i] != '\0') {
        to[i] = from[i];
        i += 1;
    }
    to[i] = '\0';
}