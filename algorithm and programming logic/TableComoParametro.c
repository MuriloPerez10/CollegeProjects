/*
programa que define uma estrutura “Pessoa” com os campos nome e idade e criar uma tabela que armazena os dados de 5 pessoas; ler valores para cada pessoa da tabela (para isso vamos criar a função lerPessoas) e depois chamar a função imprimirPessoas que apresenta os dados na tela. Note que a estrutura “Pessoa” deve ser definida antes das funções que usam a tabela do tipo “Pessoa” como parâmetro.
*/

#include <stdio.h>
#include <stdlib.h> 
// constante simbólica que representa a quantidade de pessoas da tabela
#define TAM 5 
// definiçao da estrutura Pessoa
struct Pessoa {  
       char nome[80];  
       int idade;  
}; 
// definição da função lerPessoas
void lerPessoas (struct Pessoa pessoas[]) { 
       int i;   
       for (i = 0; i < TAM; i++) {   
             printf ("Nome: ");   
             gets (pessoas[i].nome);  
             printf ("Idade: ");  
             scanf ("%d", &pessoas[i].idade);
             getchar(); 
        }
}
// definição da função imprimirPessoa 
void imprimirPessoa (struct Pessoa pessoas[]) {  
        int i = 0;  
        for (i = 0; i < TAM; i++) {   
             printf ("%s - %d\n", pessoas[i].nome, pessoas[i].idade);
        }
} 
main () {   
        // declaração da tabela do tipo Pessoa 
        struct Pessoa pessoas[TAM];  
        // chamada da funçao lerPessoas, passando a tabela como argumento
        lerPessoas (pessoas);   
        // chamada da funçao imprimirPessoas, passando a tabela como argumento 
        imprimirPessoa (pessoas);    
        printf ("\n\n");  
        system ("PAUSE");
}