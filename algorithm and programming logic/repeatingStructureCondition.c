
#include <stdio.h>
#include <stdlib.h>
//odd number counter
int main()
{
    int i,limite;
    i = 1;
    printf("escreva os numero impares que deseja ver:");
    scanf("%d",&limite);
    while(i<=limite){
        i = i+2;
        printf(" %d ",i);
    }
    system("pause");
    return 0;
}
