// HOTCOLD.c -o HOTCOLD
// ./HOTCOLD
#include <stdio.h>

int main() {
    int T;
    int input;
    scanf("%d", &T);
    for (int tc = 0; tc < T; tc++) {
        scanf("%d", &input);
        input > 20 ? printf("HOT\n") : printf("COLD\n");
    }
    return 0;
}