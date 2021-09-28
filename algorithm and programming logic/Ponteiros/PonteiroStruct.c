#include <stdio.h>
#include <stdlib.h>
// definição da estrutura
struct Pessoa {
    char nome[80];
    int idade;  
};
main () {
    // declaração e inicialização da estrutura
    struct Pessoa pessoa = {"Ana", 22};
    // declaração de um ponteiro para o tipo da estrutura
    struct Pessoa *ptr;
    // faz o ponteiro ptr apontar para a estrutura pessoa
    ptr = &pessoa;
    // imprime os dados da estrutura acessando seus campos via ponteiro
    printf ("%s - %d\n\n", (*ptr).nome, ptr->idade);
    //duas maneiras de refereciar (*ptr).nome equivale ptr->nome
    system ("PAUSE");
}