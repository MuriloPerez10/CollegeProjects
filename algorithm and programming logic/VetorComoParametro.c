#include <stdio.h>

/*
O programa ira executar um contador, para mostrar um determinada quantidade de numeros determinada pelo usuario
*/

//contador com vetor
void contag(int v[],int x){
    int i=0;
    for(i=0;i<x;i++){
        printf("%d ",i+1);
    }
}

int main()
{
    //Leitura de numeros totais para aparecer na tela
    int b;
    printf("escreva um numero: ");
    scanf("%d",&b);
    
    //chamada do procedimento
    int valor[b];
    contag(valor[b],b);
    return 0;
}
