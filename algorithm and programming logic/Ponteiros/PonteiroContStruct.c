#include <stdio.h>
#include <stdlib.h>
// definição da estrutura com campos que são ponteiros
struct PonteirosInteiros {
    int *p1;
    int *p2;    
};
main () {
    // declaração da variável do tipo PonteirosInteiros
    struct PonteirosInteiros ponteiros;
    // declaração de duas variáveis inteiras
    int x = 20, y;
    // o campos p1 de ponteiros aponta para o endereço da variável x
    ponteiros.p1 = &x;
    // o campo p2 de ponteiros aponta para o endereço da variável y
    ponteiros.p2 = &y;
    // atribuição do valor 30 ao campo p2 de ponteiros
    // note que para acessar o conteúdo do endereço apontado por p2
    // temos que colocar o símbolo * antes do nome da variável de estrutura
    *ponteiros.p2 = 30;
    // impressão das variáveis
    printf ("x = %d y = %d\n", x, y);
    printf ("Ponteiros p1 = %d p2 = %d\n\n", *ponteiros.p1, *ponteiros.p2);
    system ("PAUSE");
}