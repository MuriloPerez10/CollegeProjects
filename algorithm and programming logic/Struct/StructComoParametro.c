/*
programa que define uma estrutura “Pessoa” com os campos nome e idade; ler valores para os campos da estrutura e depois chamar a função imprimirPessoa, que apresenta os dados na tela. Note que a estrutura Pessoa deve ser definida antes da função que a usa como parâmetro.
*/

#include <stdio.h> 
#include <stdlib.h> 
// definiçao da estrutura Pessoa
struct Pessoa {   
      char nome[80];    
      int idade;  
}; 
// definição da função imprimirPessoa 
void imprimirPessoa (struct Pessoa p) {    
      printf ("%s - %d", p.nome, p.idade); 
} 
main () {  
      // declaração da variável do tipo Pessoa    
      struct Pessoa pessoa;   
      // leitura dos dados de uma Pessoa   
      printf ("Nome: ");   
      gets (pessoa.nome);  
      printf ("Idade: ");    
      scanf ("%d", &pessoa.idade);    
      printf ("\n");    
      // chamada da funçao imprimirPessoa, passando a estrutura comoargumento    
      imprimirPessoa (pessoa); 
      printf ("\n\n");   
      system ("PAUSE"); 
}