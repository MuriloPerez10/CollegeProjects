
#include <stdio.h>
#include <stdlib.h>

int main()
{
    //transformador de numeros decimal para binario
    int i,j,p,d,bina,decimal,resto[64];
    printf("escreva um numero");
    scanf("%d",&bina);
    d = bina;
    i = 0;
    //calculo de divisão para transfomção em decimal
    while (d>=10){
        resto[i] =  d % 10;
        d = d / 10;
        i++;
    }
    resto[i] = d;
    decimal = 0;
    p = 1;
    printf("\n \n %d binario em decimal = ",bina);
    
    //soma para transforma binario em decimal
    //OBS: para realizar a soma voce devera colocar o numero binario ao contrario
    for (j=i;j>=0;j++) {
        if(resto[j] != 0)
            decimal = decimal + p;
        p = p*2;
    }
    printf("O equivalente de = %d ",decimal);
    //finalização do programa
    printf("\n fim");
    system("pause");
    
    return 0;
}
