

#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

struct tnode {
    char *word;
    int count;
    struct tnode *left;
    struct tnode *right;
};

#define MAXWORD 100


struct tnode *addtree(struct tnode *, char *);
void treeprint(struct tnode *);
int getword(char *,int);
struct tnode *talloc(void);
char *strdup(char *);



/* word frequcency count */
int main() {
    struct tnode *root;
    char word[MAXWORD];

    root = NULL;
    while (getword(word, MAXWORD) != EOF) {
        if (isalpha(word[0])) {
            root = addtree(root, word);
        }
    }

    treeprint(root);
    return 0;
}




/* addtree: add a node with w, at or below p */
struct tnode *
addtree(struct tnode *p, char *w)
{
    int cond;

    if (p == NULL) {
        /* a new word has arrived */
        p = talloc();
        /* make a new node */
        p->word = strdup(w);
        p->count = 1;
        p->left = p->right = NULL;
    } else if ((cond = strcmp(w, p->word)) == 0)
        p->count++;
        /* repeated word */
    else if (cond < 0) /* less than into left subtree */
        p->left = addtree(p->left, w);
    else
        /* greater than into right subtree */
        p->right = addtree(p->right, w);
    return p;
}



void
treeprint(struct tnode *root)
{
    if (root != NULL) {
        treeprint(root->left);
        printf("%4d %s\n", root->count, root->word);
        treeprint(root->right);
    }
}




/* talloc: make a tnode */
struct tnode *
talloc(void)
{
    return (struct tnode *) malloc(sizeof(struct tnode));
}

char *
strdup(char *s)
{
    char *p;
    p = (char *) malloc(strlen(s) + 1); /* +1 for '\0' */
    if (p != NULL) {
        strcpy(p, s);
    }
    return p;
}

/*
struct tnode *talloc(void);
char *strdup(char *);

struct tnode *
addtree(struct tnode *p, char *word)
{
    int cond;

    if (p == NULL) {
        p = talloc();
        p->word = strdup(word);
        p->count = 1;
        p->left = NULL;
        p->right = NULL;
    } else if ((cond = strcmp(word, p->word)) == 0) {
        p->count++;
    } else if (cond < 0) {
        p->left = addtree(p>left, word);
    } else {
        p->right = addtree(p->right, word);
    }

    return p;
}

*/
