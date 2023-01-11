#include <stdio.h>
//#include <stdbool.h>

int main(void){
    int a = 3, b = 4, c = 2;
    int r1,r2,r3;
    int result1 = (b <= 4);
    int result2 = (c == 2);
    int result3 = a > 0;
    int result4 = b < 5;
    // bool result1 = (b <= 4);
    // bool result2 = (c == 2);
    // bool result3 = a > 0;
    // bool result4 = b < 5;

    r1 = b <=4 || c == 2; // || 는 or 이고 b<=4가 이미 true여서 안 읽음.
    r2 = (a > 0) && (b < 5); // &&라서 앞뒤 각각 체크하므로 &&읽고 앞 뒤 결과 읽고 둘 다 true여서 1
    r3 = !c; // c가 0이 아닌 2인 수로서 true인데 !붙어서 false 니까 0

    int r4 = result1 || result2;

    printf("%d, %d, %d\n",r1,r2,r3);
    printf("\nb <=4 : ",result1,"\n");
    printf("\nc == 2 : ",result2);
    printf("\na > 0 : ",(result3));
    printf("\nb < 5 : ",(result4));
    printf("r4 : %d", r4);

    return 0;

    // *p++ 체크하기. -> memcpy에서 이용.
}