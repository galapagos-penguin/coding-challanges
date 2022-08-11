// gcc will_you_survive_the_zombie_onslaught.c -o zombie -lm
// -lm is necessary to link the math library for log10
// ./zombie
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// inspired from https://stackoverflow.com/questions/36694345/strings-with-malloc-in-c
// https://stackoverflow.com/questions/5242524/converting-int-to-string-in-c
// https://stackoverflow.com/questions/8257714/how-to-convert-an-int-to-string-in-c
// https://stackoverflow.com/questions/3068397/finding-the-length-of-an-integer-in-c
char * copyStr(char message[], unsigned zombies, char message2[]) {
    // no abs function since unsigned wont be negative
    int nDigits = floor(log10(zombies)) + 1;
    char zombiesStr[nDigits]; // why not char * ???
    sprintf(zombiesStr, "%d", zombies);
    size_t len = strlen(message) + nDigits + strlen(message2); // find length of message
    char * copy;
    copy = (char *)malloc(len + 1); // dynamically allocate memory
                           /* One more char must be allocated for the null char */
    size_t i;
    for(i = 0; i < len; i++) {
        if (i < strlen(message)){
            copy[i] = message[i];  // copy characters
        }
        else if (i < (strlen(message) + nDigits)){
            copy[i] = zombiesStr[i - strlen(message)];  // copy characters
        }
        else {
            copy[i] = message2[i - (strlen(message) + nDigits)];  // copy characters
        }
    }
    copy[i] = '\0';
    printf("%s", copy);
    return copy; // return address
}

/* Return a freeable pointer */
char* zombie_shootout(unsigned zombies, unsigned distance, unsigned ammo) {
    // int / signed / signed int -> range of −2,147,483,648 to 2,147,483,647
    // unsigned / unsigned int -> range of 0 to 4,294,967,295
    // float 6 decimal digits, double 15 decimal digits.
    // printf("%u\n", remaining_zombies);
    // printf("%f\n", remaining_distance);
    unsigned remaining_zombies = zombies;
    float remaining_distance = distance; // (float)distance; not necessary
    unsigned remaining_ammo = ammo;
    while (1) {
        if (remaining_zombies == 0) {
            return copyStr("You shot all ", zombies, " zombies.");
        }
        if (remaining_distance == 0) {
            return copyStr("You shot ", zombies - remaining_zombies, " zombies before being eaten: overwhelmed.");
        }
        if (remaining_ammo == 0) {
            return copyStr("You shot ", zombies - remaining_zombies, " zombies before being eaten: ran out of ammo.");
        }
        remaining_distance = remaining_distance - 0.5;
        remaining_ammo--;
        remaining_zombies--;
    }
    return copyStr("", 0, "");
}

int main() {
    // test
    zombie_shootout(2, 1, 1);
    return 0;
}
