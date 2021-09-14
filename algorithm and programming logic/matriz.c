#include <stdio.h>
/*Programa que le um numero de notas determinadas pelo o usuario, no fim do programa dando o resultado da media dos conjuntos do numero, montandos dentro da matriz*/




int main()
{
    int nota[64],i,n,soma,media;
    printf("Quantas nosta desejar inserir? \n");
    scanf("%d", &n);
    i = 0;
    n = n - 1;
    while(i <= n){
        printf("\n digite uma nota: ");
        scanf("%d",&nota[i]);
        soma = soma + nota[i];
        i++;
    };
    i = 0;
    printf("a notas digitadas foram ");
    while(i <= n){
      printf("nota (%d) foi %d ",i,nota[i]);
      i++;
    };
    media = soma/n;
    printf("\n a media das nota e %d",media);
    
    return 0;
}