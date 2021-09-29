#include <stdio.h> 
#include <stdlib.h>
main (){     
     int vet [10] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };  
     int *p;
     //referenciando o veto ao ponteiro    
     p=vet; 
     printf ("O terceiro elemento do vetor e: %d",p[2]);
     // outra forma de referenciar o valor, nesse formato ele calculo os bytes do vetor ou seja  a cada numero somado equivale um byte, por exemplo *(p+3) = p[3]
     printf ("O terceiro elemento do vetor e: %d",*(p+2)); 
     system ("PAUSE");
}