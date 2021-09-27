/*
programa que representa uma agenda eletrônica. Um contato da agenda tem um nome e um telefone. Vamos criar um vetor de contatos, isto é, uma tabela que pode armazenar até 5 nomes. O seguinte programa solicita os dados do contato ao usuário e depois lista os contatos inseridos na agenda.
*/

#include <stdio.h>
#include <stdlib.h>
// constante simbolica que representa o tamanho da agenda
#define TAM 5
// definicao da estrutura Contato
struct Contato {   
      char nome[80];  
      char telefone[15];
};
main () { 
      // declaração da tabela agenda (vetor de contato) 
      struct Contato agenda[TAM]; 
      int i;  
      // leitura dos dados da agenda   
      // como agenda é um vetor, usamos um laço for para percorrê-lo    
      for (i = 0; i < TAM; i++) { 
            printf ("Nome: ");  
            gets (agenda[i].nome);  
            printf ("Telefone: ");   
            gets (agenda[i].telefone); 
       }    
      // impressao dos contatos da agenda 
      printf ("\n*** Lista de Contatos ***\n");   
      for (i = 0; i < TAM; i++) { 
            printf ("%s - %s\n", agenda[i].nome, agenda[i].telefone);  
      }  
      system ("PAUSE");
 }