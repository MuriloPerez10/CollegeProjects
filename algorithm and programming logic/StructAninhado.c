/*
Uma pessoa tem um nome, um endereço e uma data de nascimento. O endereço tem rua, número e bairro. No programa, vamos criar três estruturas Pessoa, Endereco e Data. O programa lê os dados de uma pessoa e depois os apresenta na tela.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
// definição da estrutura Data 
struct Data {   
      int dia, mes, ano; 
};
// definição da estrutura Endereco
struct Endereco {  
      char rua[100];  
      char numero[10];  
      char bairro[30];
}; 
// definição da estrutura Pessoa 
struct Pessoa {    
      char nome[80];  
      struct Endereco endereco; 
      struct Data dataNasc; 
};
main () {  
      // declaração da variavel do tipo Pessoa   
      struct Pessoa umaPessoa;
      // leitura do nome   
      printf ("Nome: ");  
      gets (umaPessoa.nome);   
      // leitura do endereco  
      printf ("Rua: ");  
      gets (umaPessoa.endereco.rua);   
      printf ("Numero: ");
      gets (umaPessoa.endereco.numero);  
      printf ("Bairro: ");    
      gets (umaPessoa.endereco.bairro);
      // leitura da data de nascimento    
      printf ("Dia: ");   
      scanf ("%d", &umaPessoa.dataNasc.dia);  
      printf ("Mes: ");  
      scanf ("%d", &umaPessoa.dataNasc.mes);
      printf ("Ano: ");
      scanf ("%d", &umaPessoa.dataNasc.ano); 
      // impressao dos dados da pessoa  
      printf ("\n\n*** Dados da Pessoa *** \n");   
      printf ("Nome: ");   
      puts (umaPessoa.nome);  
      printf ("Endereco: %s, ", umaPessoa.endereco.rua); 
      printf ("%s - ", umaPessoa.endereco.numero);  
      printf ("%s\n", umaPessoa.endereco.bairro);
      printf ("Data de Nasscimento: %d/", umaPessoa.dataNasc.dia);
      printf ("%d/", umaPessoa.dataNasc.mes); 
      printf ("%d\n\n", umaPessoa.dataNasc.ano);  
      system ("PAUSE");   
} 