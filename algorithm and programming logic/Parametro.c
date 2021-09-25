/*
1 - Uma função com dois parâmetros, por valor, denominados “ini” e “fim”. É feito o cálculo e o valor da soma de todos os números pares entre “ini” e “fim” é retornado.

2- Um procedimento com dois parâmetros, sendo o primeiro “opcao” por valor e o segundo “n” por referência. Se “opcao” é igual a 1, então, é feito o cálculo do dobro do valor de “n”. Se “opcao” é igual a 2, o triplo do valor de “n” é calculado. O valor de n, alterado por referência dentro do procedimento, é mostrado no "main".
*/

#include <stdio.h>
#include <stdlib.h>
 
int soma_valores (int ini, int fim) {
       int i, soma = 0;
       for (i=ini;i<=fim;i++)
            soma = soma + i;
       return (soma);  
}
 
void calcula_dobro_triplo (int opcao, int *n) {
       if (opcao==1)
           *n = *n * 2;
       else if (opcao==2)
           *n = *n * 3;
} 
 
main () {
        int ini = 1, fim = 10, n=4, soma, opcao;
               
        soma = soma_valores (ini, fim);
        printf ("\n Valor da soma = %d", soma);
 
        printf ("\n Digite a opcao =");
        scanf ("%d", &opcao);
        calcula_dobro_triplo (opcao, &n);
        printf("Valor de n = %d", n);
 
        system ("pause");        
}