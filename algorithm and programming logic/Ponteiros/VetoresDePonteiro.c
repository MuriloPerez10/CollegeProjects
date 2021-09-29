/*
O programa a seguir mostra a utilização de um vetor que irá armazenar e mostrar na tela os endereços de memória de 5 números inteiros.
*/

#include <stdio.h>
#include <stdlib.h>
 
main () {  
    int *vet [5];  
    int v1=3, v2=5, v3=8, v4=10, v5=15, i;  
    vet [0] = &v1;    
    vet [1] = &v2;  
    vet [2] = &v3;   
    vet [3] = &v4;   
    vet [4] = &v5;      
 
    for (i=0; i<5; i++) {   
          printf ("\n Conteudo de vet[%d] = %p", i, vet[i]);  
    }  
    system ("PAUSE"); 
}