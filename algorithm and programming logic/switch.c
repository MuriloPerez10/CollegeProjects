#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n1,n2,escolha,resultado;
    while(1){
    printf(">>>Bem vindo a calculadora<<< \n escolha uma opcao");
    printf("\n digite um numero:");
    scanf("%d",&n1);
    printf(" digite um numero:");
    scanf("%d",&n2);
    
    printf("\n escolha uma opcao para realizar com esses numeros");
    printf("\n 0- soma \n 1-subtração \n 2-divisao \n 3-multiplicacao \n");
    scanf("%d",&escolha);
    switch(escolha){
        case 0: resultado = n1 + n2; break;
        case 1: resultado = n1 - n2; break;
        case 2: resultado = n1 / n2; break;
        case 3: resultado = n1 * n2; break;
        case 5: return;
    }
    printf("o resultado da operacao e %d",resultado);}
    system("pause")
    return 0;
}
