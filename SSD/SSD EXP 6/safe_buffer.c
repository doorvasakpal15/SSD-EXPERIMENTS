#include <stdio.h>
#include <string.h>

int main() {

    char name[20];

    printf("Enter your name (maximum 19 characters): ");

    fgets(name, sizeof(name), stdin);

    /*
       If newline is not present, the input was longer
       than the buffer could hold.
    */

    if (strchr(name, '\n') == NULL) {

        printf("\n");
        printf("BUFFER OVERFLOW ATTEMPT DETECTED!\n");
        printf("Input exceeded the maximum buffer size.\n");
        printf("Excess input was safely limited.\n");

        // Clear remaining input
        int ch;

        while ((ch = getchar()) != '\n' && ch != EOF) {
            // discard extra characters
        }

    } else {

        name[strcspn(name, "\n")] = '\0';

        printf("\nSafe input: %s\n", name);
    }

    return 0;
}