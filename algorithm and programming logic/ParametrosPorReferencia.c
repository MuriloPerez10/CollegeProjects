/*
A passagem de parâmetro por referência ocorre quando o parâmetro real recebe o conteúdo do parâmetro formal e, após um certo processamento dentro do módulo, o parâmetro formal reflete a alteração de seu valor junto ao parâmetro real. Qualquer modificação feita no parâmetro formal implica em alteração do parâmetro real correspondente. A alteração efetuada é devolvida para a rotina chamadora.
*/

#include <stdio.h>
#include <stdlib.h>
 
void dobro (int *n)
{
         *n = 2*(*n);
         printf ("\n Valor de n = %d", *n);
}
 
main ()   
{
        int n = 8;
        dobro (&n);
        printf ("\n Valor de n = %d", n);
        system ("PAUSE");
}